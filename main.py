
import os
import asyncio
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from groq import AsyncGroq
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise RuntimeError("GROQ_API_KEY is missing from .env")

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)

# Speech-to-text client
groq_client = AsyncGroq(api_key=API_KEY)

# Translation model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=API_KEY,
    temperature=0,
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Translate the user's text into {language}. "
        "Return only the translation. Preserve the meaning."
    ),
    ("human", "{text}"),
])

translation_chain = prompt | model | StrOutputParser()


@app.get("/")
async def home():
    html_path = Path("static/index.html")
    return HTMLResponse(html_path.read_text(encoding="utf-8"))


async def transcribe_audio(audio: bytes) -> str:
    result = await groq_client.audio.transcriptions.create(
        file=("chunk.webm", audio, "audio/webm"),
        model="whisper-large-v3-turbo",
        response_format="text",
        temperature=0,
    )

    return result.strip()


async def translate_text(text: str, language: str) -> str:
    return await translation_chain.ainvoke({
        "text": text,
        "language": language,
    })



@app.websocket("/ws")
async def speech_translator(websocket: WebSocket):
    await websocket.accept()

    try:
        config = await websocket.receive_json()
        language = config.get("language", "Hindi").strip()

        await websocket.send_json({
            "type": "status",
            "message": f"Translating into {language}",
        })

        while True:
            # Wait for the next audio chunk.
            audio = await websocket.receive_bytes()

            if not audio:
                continue

            try:
                transcript = await transcribe_audio(audio)

                if not transcript:
                    continue

                translated = await translate_text(
                    transcript,
                    language,
                )

                # The client may have disconnected while
                # transcription or translation was running.
                await websocket.send_json({
                    "type": "result",
                    "original": transcript,
                    "translated": translated,
                })

            except WebSocketDisconnect:
                # The browser closed the connection.
                break

            except Exception as exc:
                print("Chunk processing error:", repr(exc))

                # Do not attempt another send if the client
                # has disconnected.
                try:
                    await websocket.send_json({
                        "type": "error",
                        "message": "Could not process this audio chunk.",
                    })
                except (WebSocketDisconnect, RuntimeError):
                    break

    except WebSocketDisconnect:
        print("Client disconnected.")

    except RuntimeError as exc:
        print("WebSocket connection closed:", exc)

    finally:
        print("Speech translation session ended.")

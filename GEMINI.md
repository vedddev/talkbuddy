@'
# TalkBuddy - Project Instructions

## Project Overview
TalkBuddy is a real-time speech translation web application.
Users speak into a microphone, receive speech transcription,
translate it into a selected language, and hear the translated output.

## Technology Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy 2.0
- Alembic
- Groq Whisper for speech-to-text
- LangChain and Groq LLM for translation
- React, TypeScript and Tailwind CSS (planned frontend)

## Development Rules
1. Understand the existing code before making changes.
2. Do not unnecessarily rewrite working features.
3. Keep the existing speech translation functionality working.
4. Write clean, modular, maintainable code.
5. Use asynchronous functions where appropriate.
6. Follow Python naming conventions.
7. Add type hints to Python functions.
8. Handle errors properly.
9. Never hardcode API keys or passwords.
10. Store secrets in the .env file.
11. Never expose secrets in frontend code.
12. Avoid unnecessary dependencies.

## Architecture
- Separate API routes, database models, schemas and services.
- Keep authentication separate from translation logic.
- Use SQLAlchemy for database operations.
- Use Pydantic for request and response validation.
- Use WebSockets for live speech translation.
- Keep database migrations in Alembic.

## Security
- Hash passwords using Argon2id.
- Use secure HTTP-only cookies for authentication.
- Validate user sessions.
- Protect authenticated WebSocket connections.
- Never trust user IDs supplied by the frontend.
- Apply appropriate input validation and rate limiting.

## AI Features
- Use Groq Whisper for transcription.
- Use the configured Groq LLM for translation.
- Preserve the meaning and context of the original speech.
- Handle transcription and translation failures gracefully.
- Do not save microphone audio by default.

## Working With Multiple Agents
- Follow the shared architecture and API contracts.
- Do not modify another agent's files unnecessarily.
- Communicate required API changes before implementing them.
- Do not create duplicate models, routes or services.
- Run relevant tests after making changes.

## Before Completing a Task
1. Explain what files will be changed.
2. Implement the requested functionality.
3. Check imports and dependencies.
4. Run relevant tests.
5. Explain what was implemented and any remaining issues.

## Important
Prefer simple, reliable solutions over unnecessary complexity.
Do not claim a feature is implemented unless it actually works.
'@ | Set-Content -Encoding UTF8 GEMINI.md
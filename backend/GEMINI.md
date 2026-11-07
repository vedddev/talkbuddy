@'
# Backend Development Instructions

## Backend Stack
- FastAPI
- Python
- PostgreSQL
- SQLAlchemy 2.0
- Alembic
- Pydantic
- Groq API
- LangChain

## Folder Responsibilities

- core/: Configuration and security utilities.
- database/: Database connection and base models.
- models/: SQLAlchemy database models.
- schemas/: Pydantic schemas.
- api/: REST API routes.
- services/: Business logic and AI integrations.
- dependencies/: Authentication and shared dependencies.
- websockets/: WebSocket communication.
- tests/: Backend tests.

## Coding Rules
1. Use async endpoints when appropriate.
2. Keep business logic out of API route files.
3. Use dependency injection.
4. Use Pydantic schemas for validation.
5. Use SQLAlchemy 2.0 patterns.
6. Handle database transactions correctly.
7. Use environment variables for configuration.
8. Never expose internal errors or secrets to clients.
9. Add appropriate HTTP status codes.
10. Write tests for important functionality.

## Authentication
- Implement registration and login.
- Hash passwords with Argon2id.
- Use secure HTTP-only session cookies.
- Implement logout and session revocation.
- Validate authentication for protected endpoints.
- Authenticate WebSocket connections securely.

## Translation
- Keep transcription and translation in separate services.
- Use Groq Whisper for speech recognition.
- Use the configured Groq LLM for translation.
- Handle empty audio, transcription errors and API failures.
- Keep the existing working translation pipeline intact.

## Database
- Use PostgreSQL.
- Use SQLAlchemy models.
- Manage schema changes with Alembic.
- Associate user data with the authenticated user.
- Do not store raw audio unless explicitly requested.

## Testing
- Test authentication endpoints.
- Test database operations.
- Test translation services.
- Test WebSocket connection and disconnection.
- Test unauthorized access.

## Important
Inspect existing code before modifying it.
Do not replace working implementations without a clear reason.
'@ | Set-Content -Encoding UTF8 backend/GEMINI.md
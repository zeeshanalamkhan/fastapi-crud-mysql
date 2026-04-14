import uuid
from fastapi import Request
from app.core.config import CORRELATION_HEADER
from app.core.context.context import correlation_id_ctx

async def correlation_middleware(request: Request, call_next):
    correlation_id = request.headers.get(CORRELATION_HEADER)

    if not correlation_id:
        correlation_id = str(uuid.uuid4())

    # Always set the correlation ID in context (whether from header or generated)
    correlation_id_ctx.set(correlation_id)

    response = await call_next(request)

    response.headers[CORRELATION_HEADER] = correlation_id

    return response
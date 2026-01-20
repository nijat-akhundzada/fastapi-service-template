import logging
import uuid

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

logger = logging.getLogger("request")


class RequestIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-Id") or str(uuid.uuid4())
        request.state.request_id = request_id

        # inject request_id into logs (simple approach)
        extra = {"request_id": request_id}
        logger.info("request.start", extra=extra)

        response = await call_next(request)
        response.headers["X-Request-Id"] = request_id

        logger.info("request.end", extra=extra)
        return response

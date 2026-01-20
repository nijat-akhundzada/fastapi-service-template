from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.api.router import api_router
from app.core.errors import AppError, to_error_payload
from app.core.logging import setup_logging
from app.core.middleware import RequestIdMiddleware
from app.core.settings import settings


def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(title=settings.service_name)

    @app.exception_handler(AppError)
    async def app_error_handler(request: Request, exc: AppError):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=to_error_payload(exc))

    app.add_middleware(RequestIdMiddleware)
    app.include_router(api_router)
    return app


app = create_app()

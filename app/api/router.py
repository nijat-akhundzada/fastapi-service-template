from fastapi import APIRouter

from .routes.examples import router as examples_router
from .routes.health import router as health_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health_router, tags=["system"])
api_router.include_router(examples_router, tags=["examples"])

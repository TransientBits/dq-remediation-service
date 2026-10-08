from fastapi import APIRouter

from dq_remediation.api.endpoints.health import router as health_router

api_router = APIRouter(prefix="/api")
api_router.include_router(health_router)

from fastapi import FastAPI

from dq_remediation.api.router import api_router
from dq_remediation.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.project_name,
        version="0.1.0",
        description="SAP Data Quality remediation service",
    )
    app.include_router(api_router)
    return app


app = create_app()

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_env: str = "development"
    app_debug: bool = False
    project_name: str = "dq-remediation-service"

    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "dq_remediation"
    database_user: str = "postgres"
    database_password: str = "postgres"

    service_bus_connection_string: str = ""
    service_bus_issue_subscription: str = ""
    service_bus_issue_topic: str = ""

    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = ""

    openai_api_key: str = Field(default="", repr=False)
    openai_model: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()

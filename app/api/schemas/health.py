from typing import Literal

from pydantic import BaseModel


class HealthStatus(BaseModel):
    status: Literal["ok"] = "ok"


class HealthResponse(HealthStatus):
    service: str
    version: str
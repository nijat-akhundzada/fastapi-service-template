from dataclasses import dataclass
from enum import Enum

class ErrorCode(str, Enum):
    VALIDATION_ERROR = "validation_error"
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"
    FORBIDDEN = "forbidden"
    CONFLICT = "conflict"
    INTERNAL_ERROR = "internal_error"

@dataclass(frozen=True)
class AppError(Exception):
    code: str
    message: str
    details: dict | None = None


def to_error_payload(err: AppError) -> dict:
    return {"error": {"code": err.code, "message": err.message, "details": err.details or {}}}

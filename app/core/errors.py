from dataclasses import dataclass


@dataclass(frozen=True)
class AppError(Exception):
    code: str
    message: str
    details: dict | None = None


def to_error_payload(err: AppError) -> dict:
    return {"error": {"code": err.code, "message": err.message, "details": err.details or {}}}

import logging

from pythonjsonlogger import json

from .settings import settings


def setup_logging() -> None:
    root = logging.getLogger()
    root.setLevel(settings.log_level)

    handler = logging.StreamHandler()
    formatter = json.JsonFormatter(
        "%(levelname)s %(name)s %(message)s %(asctime)s %(request_id)s"
    )
    handler.setFormatter(formatter)

    root.handlers.clear()
    root.addHandler(handler)

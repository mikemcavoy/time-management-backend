import logging
from pathlib import Path
from fastapi import FastAPI
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from .common.custom_logging import CustomizeLogger
from .common.http_exception_handler import http_exception_handler
from .common.http_validation_exception_handler import http_validation_exception_handler
from .controller.todo import router as todo_router
from .db.configure_db import test_db_connection

logger = logging.getLogger(__name__)
config_path = Path(__file__).with_name("logging_config.json")


def create_app():
    app = FastAPI()

    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger

    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, http_validation_exception_handler)

    app.include_router(todo_router, prefix='')

    test_db_connection()

    return app

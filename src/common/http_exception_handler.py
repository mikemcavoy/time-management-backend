from starlette.exceptions import HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse


async def http_exception_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": exc.status_code, "msg": exc.detail}
    )

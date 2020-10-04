from fastapi import status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def http_validation_exception_handler(
        _: Request, exc: RequestValidationError) -> JSONResponse:

    formatted_errors = []
    for err in exc.errors():
        value = ' '.join(err['loc'])
        formatted_errors.append(value + ' ' + err['msg'])

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "msg": formatted_errors
        }
    )

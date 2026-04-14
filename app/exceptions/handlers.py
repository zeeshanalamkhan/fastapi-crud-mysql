from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.custom_exceptions import UserNotFoundException, HeaderMissingException, UnauthorizedUserException

def user_not_found_exception_handler(request: Request, exec: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": exec.message}
    )

def header_missing_exception_handler(request: Request, exec: HeaderMissingException):
    return JSONResponse(
        status_code=400,
        content={"message": exec.message}
    )


def unauthorized_user_exception_handler(request: Request, exec: UnauthorizedUserException):
    return JSONResponse(
        status_code=401,
        content={"message": exec.message}
    )
from fastapi import FastAPI
from sqlmodel import SQLModel
from app.db.session import engine
from app.routes import user_routes
from app.exceptions.custom_exceptions import UserNotFoundException, HeaderMissingException, UnauthorizedUserException
from app.exceptions.handlers import user_not_found_exception_handler, header_missing_exception_handler, unauthorized_user_exception_handler
from app.middleware.logging_middleware import logging_middleware
from app.core.logging_config import setup_logging
from app.middleware.correlation_middleware import correlation_middleware

app = FastAPI()

SQLModel.metadata.create_all(engine)
setup_logging()

# IMPORTANT: Correlation middleware must come BEFORE logging middleware
app.middleware("http")(correlation_middleware)
app.middleware("http")(logging_middleware)

app.add_exception_handler(UserNotFoundException, user_not_found_exception_handler)
app.add_exception_handler(HeaderMissingException, header_missing_exception_handler)
app.add_exception_handler(UnauthorizedUserException, unauthorized_user_exception_handler)
app.include_router(user_routes.router)
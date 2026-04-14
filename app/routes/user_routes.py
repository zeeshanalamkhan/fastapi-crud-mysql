import logging
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.models.user_model import User
from app.services import user_service
from app.exceptions.custom_exceptions import UserNotFoundException
from app.dependencies.auth import jwt_auth_interceptor
from app.models.login_request_model import LoginRequest
from app.core.security.security import create_token


router = APIRouter()

logger = logging.getLogger(__name__)

@router.post("/auth/token")
def generate_token(request: LoginRequest):
    logger.info("Fetching token")
    token = create_token({"sub": request.username})
    return {
        "access_token": token,
        "token_type": "Bearer"
    }

@router.post("/users", response_model=User, dependencies=[Depends(jwt_auth_interceptor)])
def create_user(user: User, db: Session = Depends(get_session)):
    logger.info("Creating user")
    return user_service.create_user(db, user)

@router.get("/users", response_model=list[User], dependencies=[Depends(jwt_auth_interceptor)])
def get_users(db:Session = Depends(get_session)):
    logger.info("Fetching all users")
    return user_service.get_users(db)

@router.get("/users/{user_id}", dependencies=[Depends(jwt_auth_interceptor)])
def get_user(user_id: int, db: Session = Depends(get_session)):
    logger.info("Fetching user by id")
    user = user_service.get_user(db, user_id)
    if not user:
        logger.error("user not found")
        raise UserNotFoundException("User not found!")
    return user

@router.put("/users", dependencies=[Depends(jwt_auth_interceptor)])
def update_user(user: User, db: Session = Depends(get_session)):
    logger.info("updating user")
    user = user_service.update_user(db, user)
    if not user:
        logger.error("user not found")
        raise UserNotFoundException("User not found!")
    return user

@router.delete("/users/{user_id}", dependencies=[Depends(jwt_auth_interceptor)])
def delete_user(user_id: int, db: Session = Depends(get_session)):
    logger.info("deleting user")
    user = user_service.delete_user(db, user_id)
    if not user:
        logger.error("user not found")
        raise UserNotFoundException("User not found!")
    return {"message": "Deleted"}
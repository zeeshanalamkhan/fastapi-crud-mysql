from fastapi import Header, HTTPException
from app.core.security.security import verify_token
from app.exceptions.custom_exceptions import HeaderMissingException, UnauthorizedUserException

def jwt_auth_interceptor(authorization: str = Header(None)):
    if not authorization:
        raise HeaderMissingException("Missing Authorization header")
    
    try:
        # Bearer <token>
        token = authorization.split(" ")[1]
        payload = verify_token(token)
        return payload
    except Exception as e:
        raise UnauthorizedUserException(str(e))
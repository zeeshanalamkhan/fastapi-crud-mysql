import jwt
from datetime import datetime, timedelta
from app.core.config import SECRET_KEY, ALGORITHM, TOKEN_EXPIRE_TIME_MINUTES

def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_TIME_MINUTES)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise Exception("Token expired!")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
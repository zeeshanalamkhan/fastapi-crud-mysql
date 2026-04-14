from sqlmodel import Session, select
from app.models.user_model import User

def save(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def  find_all(db: Session):
    return db.exec(select(User)).all()

def find_by_id(db: Session, user_id: int):
    return db.get(User, user_id)

def delete(db: Session, user: User):
    db.delete(user)
    db.commit()
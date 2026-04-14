from app.repositories import user_repo

def create_user(db, user):
    return user_repo.save(db, user)

def get_users(db):
    return user_repo.find_all(db)

def get_user(db, user_id):
    return user_repo.find_by_id(db, user_id)

def update_user(db, user):
    user_id = user.id
    existing_user = user_repo.find_by_id(db, user_id)
    if existing_user:
        existing_user.name = user.name
        existing_user.email = user.email
        user_repo.save(db, existing_user)
    return user

def delete_user(db, user_id):
    user = user_repo.find_by_id(db, user_id)
    if user:
        user_repo.delete(db, user)
    return user
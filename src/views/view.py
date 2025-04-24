from fastapi import HTTPException
from src.models.student import db


def get_users_view():
    users = db.get_all_users()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

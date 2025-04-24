from fastapi import APIRouter
from src.models.student import Student, db
from src.views.view import get_users_view

router = APIRouter(prefix="/v1")


@router.post("/users", response_model=Student)
async def create_user(user: Student):
    db.add_user(user)
    return user


@router.get("/users", response_model=list[Student])
async def get_users():
    return get_users_view()

from fastapi import APIRouter, HTTPException
from sqlalchemy import text

from ..database import engine
from ..schema import UserCreate, UserRead

router = APIRouter()

@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    with engine.begin() as conn:
        result = conn.execute(
            text("INSERT INTO users (name, email) VALUES (:name, :email)"),
            {"name": user.name, "email": user.email}
        )
        user_id = result.lastrowid
        return {**user.model_dump(), "id": user_id}

@router.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT id, name, email FROM users WHERE id = :id"),
            {"id": user_id}
        ).mappings().fetchone()
        if result is None:
            raise HTTPException(status_code=404, detail="User not found")
        return dict(result)

@router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserCreate):
    with engine.begin() as conn:
        result = conn.execute(
            text("UPDATE users SET name = :name, email = :email WHERE id = :id"),
            {**user.model_dump(), "id": user_id}
        )
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return {**user.model_dump(), "id": user_id}

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    with engine.begin() as conn:
        result = conn.execute(
            text("DELETE FROM users WHERE id = :id"),
            {"id": user_id}
        )
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted"}
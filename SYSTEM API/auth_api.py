from fastapi import APIRouter
from passlib.context import CryptContext

router = APIRouter(tags=["auth"])
pwd_context = CryptContext(schemes=["bcrypt"])


@router.post("/signup")
def signup(password: str):
    hashed_password = pwd_context.hash(password)
    return {"message": "User created successfully", "hashed_password": hashed_password}

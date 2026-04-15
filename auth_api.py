from fastapi import FastAPI
from passlib.context import CryptContext
app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"])
@app.post("/signup")
def signup(password: str):
    hashed_password = pwd_context.hash(password)
    return {"message": "User created successfully", "hashed_password": hashed_password}
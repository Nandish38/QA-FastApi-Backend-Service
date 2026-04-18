from fastapi import FastAPI

from Upload import router as upload_router
from auth_api import router as auth_router

app = FastAPI()
app.include_router(upload_router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "Hello nandish, your Fast Api"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def say_hello():
    return {"message": "Hello from FastAPI"}

@app.post("/register")
def register_user(user: dict):
    return {
        "status": "success",
        "received_data": user
    }


# Model definition using Pydantic
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    age: int

# Use Model in POST API

@app.post("/re")
def register_user_model(user: User):
    """Register a new user"""

    return {
        "status": "success",
        "received_data": user
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }


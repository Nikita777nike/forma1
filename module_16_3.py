from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}

@app.get("/users")
async def get_user() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: str=Path(min_length=5, max_length=20, description="Enter your username", example="UrbanUser"),
                   age: int=Path(ge=18, le=100, description="Enter your age", example="44")) -> str:
    user_id = str(int(max(map(int, users.keys()))+1))
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str=Path(min_length=1, max_length=2000, description="Enter id", example="1"),
                username: str=Path(min_length=5, max_length=20, description="Enter your username", example="UrbanUser"),
                age: int=Path(ge=18, le=100, description="Enter your age", example="44")) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} updated"


@app.delete("/user/{user_id}")
def delete_user(user_id: str=Path(min_length=1, max_length=2000, description="Enter id", example="1")) -> str:
    del users[user_id]
    return f"User {user_id} deleted"
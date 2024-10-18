from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def home_page() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin_page() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def id_page(user_id: int=Path(ge=0, le=100, description="Enter user id", example="50")) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def user_page(username: str=Path(min_length=5, max_length=20, description="Enter your username", example="UrbanUser"),
                   age: int=Path(ge=18, le=120, description="Enter your age", example="44")) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

from fastapi import APIRouter
from database import gamecategoryservice
from pydantic import BaseModel

game_category_router = APIRouter(prefix='/gamecategory', tags=['Управление категориями'])

@game_category_router.post("/api/gamecategory")
async def add_category(text: str):
    add_game_category = gamecategoryservice.add_category(text)
    return "Succesfuly added"

@game_category_router.get("/api/gamecategory")
async def get_all_category():
    all_category = gamecategoryservice.get_all_category()
    return all_category

@game_category_router.get("/api/exactgamecategory")
async def get_exact_category(category: int):
    exact_category = gamecategoryservice.get_exact_category(category)
    if exact_category:
        return exact_category
    return "Fathulla"

@game_category_router.put("/api/gamecategory")
async def change_category(id: int, category: str):
    change = gamecategoryservice.change_category(id, category)
    if change:
        return change
    return "Fathulla"
@game_category_router.delete("/api/gamecategory")
async def delete_category_game(category):
    delete = gamecategoryservice.delete_category(category)
    if delete:
        return delete
    return "Fathulla"

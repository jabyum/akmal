from fastapi import APIRouter
from database import gameservice
from pydantic import BaseModel

game_router = APIRouter()


class Game(BaseModel):
    game_name: str
    category: int
    game_desc: str
    like: int
    price: float


@game_router.post("/api/games")
async def add_game(gamemodel: Game):
    gamedata = dict(gamemodel)
    add_games = gameservice.add_game(**gamedata)
    return "sUCCESFULY ADDED"


@game_router.get('/api/games')
async def get_all_game():
    game = gameservice.get_all_games()
    return game

@game_router.get('/api/exact_game')
async def get_game(game_name: str):
    game = gameservice.get_game_by_name(game_name)
    if game:
        return game
    return 'NETU'
@game_router.put('/api/games')
async def change_game(game_id: int, change_info: str, new_data):
    info = gameservice.game_change(game_id, change_info, new_data)
    if info:
        return info
    return "Fathulla"
@game_router.delete("/api/games")
async def delete_game(game_id: int):
    delete = gameservice.delete_exact_game(game_id)
    if delete:
        return delete
    return "Fathulla"

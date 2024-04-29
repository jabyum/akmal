from fastapi import FastAPI
from api.game_api.games import game_router
from database import Base, engine
from api.user_api.user_api import user_router
from api.gamecategory.game_category import game_category_router
Base.metadata.create_all(bind=engine)


app = FastAPI(docs_url='/')
app.include_router(game_router)
app.include_router(user_router)
app.include_router(game_category_router)
from database.models import Games
from database import get_db

def add_game(game_name, category, price, game_desc, like):
    db= next(get_db())
    add_games = Games(game_name=game_name, category=category, price=price,
                      game_desc=game_desc, like=like)
    db.add(add_games)
    db.commit()
    return "Успешно добавлено"

def game_change(id, change_info, newdata):
    db = next(get_db())
    change = db.query(Games).filter_by(id=id).first()
    if change:
        if change_info == "game_name":
            change.game_name = newdata
        elif change_info == "category":
            change.category = newdata
        elif change_info == "price":
            change.price = newdata
        elif change_info == "game_desc":
            change.game_desc = newdata
        elif change_info == "like":
            change.like = newdata
        db.commit()
        return "Информация изменена"
    return "Error"


def get_all_games():
    db = next(get_db())
    all_info = db.query(Games).all()
    return all_info

def get_game_by_name(game_name):
    db = next(get_db())
    exact_game = db.query(Games).filter_by(game_name=game_name).first()
    if exact_game:
        return exact_game
    return False
def delete_exact_game(game_id):
    db = next(get_db())
    exact_delete = db.query(Games).filter_by(id=game_id).delete()
    if exact_delete:
        return "Deleted"
    return "Fathulla"
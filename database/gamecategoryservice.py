from database.models import GamesCategory
from database import get_db

def add_category(category):
    db = next(get_db())
    add_category = GamesCategory(category=category)
    db.add(add_category)
    db.commit()
    return "Succesfuly added"
def change_category(id, category):
    db = next(get_db())
    info = db.query(GamesCategory).filter_by(id=id).first()
    if info:
        info.category = category
        db.commit()
        return "Changed"
    return "Fathulla"
def get_all_category():
    db = next(get_db())
    all_info = db.query(GamesCategory).all()
    return all_info
def get_exact_category(category):
    db = next(get_db())
    exact_category = db.query(GamesCategory).filter_by(id=category).first()
    if exact_category:
        return exact_category
    return "Fathulla"

def delete_category(category):
    db = next(get_db())
    delete_exact_category = db.query(GamesCategory).filter_by(category=category).delete()
    if delete_exact_category:
        return "Deleted"
    return "Fathulla"
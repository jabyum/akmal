from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base


class GamesCategory(Base):
    __tablename__ = "gamescategory"
    id = Column(Integer, autoincrement=True, primary_key=True)
    category = Column(String, nullable=False)


class Games(Base):
    __tablename__ = "games"
    id = Column(Integer, autoincrement=True, primary_key=True)
    game_name = Column(String, nullable=False)
    category = Column(String, ForeignKey("gamescategory.category"))
    game_desc = Column(String, nullable=False)
    like = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    game_categorys_fk = relationship(GamesCategory, lazy="subquery")
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    friend_id =Column(Integer, ForeignKey('users.id'))
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)
    game_count = Column(Integer, ForeignKey("games.id"))
    friend = relationship('User', remote_side=[id])
    game = relationship(Games, lazy="subquery")



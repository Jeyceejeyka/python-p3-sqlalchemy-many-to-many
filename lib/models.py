from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'game'  # ✅ Make sure this name matches your expected table name

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    platform = Column(String)
    price = Column(Float)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    reviews = relationship("Review", back_populates="game")
    users = relationship("User", secondary="reviews", back_populates="games")


class User(Base):
    __tablename__ = 'user'  # ✅ Make sure this name matches

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    reviews = relationship("Review", back_populates="user")
    games = relationship("Game", secondary="reviews", back_populates="users")


class Review(Base):
    __tablename__ = 'review'  # ✅ Make sure this name matches

    id = Column(Integer, primary_key=True)
    score = Column(Integer, nullable=False)
    comment = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    game_id = Column(Integer, ForeignKey('games.id'))  # ✅ Ensure FK references correctly
    user_id = Column(Integer, ForeignKey('users.id'))  # ✅ Ensure FK references correctly

    game = relationship("Game", back_populates="reviews")
    user = relationship("User", back_populates="reviews")

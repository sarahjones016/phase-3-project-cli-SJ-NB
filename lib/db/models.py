from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'
    __table_args__ = (PrimaryKeyConstraint('id'), )

    id = Column(Integer())
    star_rating = Column(Integer())
    genre_id = Column(Integer())
    fan_id = Column(Integer())

def __repr__(self):
    return f"ID: {self.id}," + \
    f"Star Rating: {self.star_rating}" + \
    f"Genre ID: {self.genre_id}" + \
    f"Fan ID: {self.fan_id}"
from sqlalchemy import (PrimaryKeyConstraint, ForeignKey, Column, Integer, Float, String, DateTime)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Fan(Base):
    __tablename__ = 'fans'
    __table_args__ = (PrimaryKeyConstraint('id'), )

    id = Column(Integer())
    first_name = Column(String())
    last_name = Column(String())

def __repr__(self):
    return f"ID: {self.id}," + \
    f"First Name: {self.first_name}" + \
    f"Last Name: {self.last_name}"




class Review(Base):
    __tablename__ = 'reviews'
    __table_args__ = (PrimaryKeyConstraint('id'), )

    id = Column(Integer())
    star_rating = Column(Integer())
    genre_id = Column(Integer(), ForeignKey('genres.id'))
    fan_id = Column(Integer(), ForeignKey('fans.id'))

    fan = relationship('Fan', backref=backref('fans'))
    genre = relationship('Genre', backref=backref('genres'))

def __repr__(self):
    return f"ID: {self.id}," + \
    f"Star Rating: {self.star_rating}" + \
    f"Genre ID: {self.genre_id}" + \
    f"Fan ID: {self.fan_id}"




class Genre(Base):
    __tablename__ = 'genres'
    __table_args__ = (PrimaryKeyConstraint('id'), )

    id = Column(Integer())
    avg_bpm = Column(Integer())
    style = Column(String())
    prodominent_instrument = Column(String())
    commonly_known = Column(String())

def __repr__(self):
    return f"ID: {self.id}," + \
    f"Average BPM: {self.average_bpm}" + \
    f"Style: {self.style}" + \
    f"Prodominent Instrument: {self.prodominent_instrument}" + \
    f"Commonly Known: {self.commonly_known}"



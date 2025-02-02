import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from datetime import datetime
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    subscription_date = Column(DateTime, default=datetime.utcnow)

    favorites = relationship("Favorite", back_populates="user")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(String(250))

    favorites = relationship("Favorite", back_populates="planet")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250))
    homeworld = Column(String(250))
    gender = Column(String(250))
    birth_year = Column(String(250))

    favorites = relationship("Favorite", back_populates="character")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)

    user = relationship("User", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")

# Generar el diagrama de la base de datos
render_er(Base, 'starwars_blog_diagram.png')

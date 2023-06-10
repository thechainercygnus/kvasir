from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class dog(Base):
    __tablename__ = "dog"
    dog_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Float)
    biography = Column(String)


class breed(Base):
    __tablename__ = "breed"
    breed_id = Column(Integer, primary_key=True)
    breed_name = Column(String)

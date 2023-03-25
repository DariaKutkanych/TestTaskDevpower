from db.db import Base, db
from sqlalchemy import Column, Integer, String, Float, DateTime


class Population(Base):

    __tablename__ = "population"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    country = Column(String(250), nullable=False, unique=True)
    numbers = Column(Integer, nullable=False)

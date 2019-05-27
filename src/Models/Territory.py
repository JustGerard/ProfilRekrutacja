from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.Models.BaseModel import BaseModel


class Territory(BaseModel.Base):
    __tablename__ = 'territory'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    years = relationship('Year', backref="territory")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Territory('%s')>" % self.name

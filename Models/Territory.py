from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from Controlers.DatabaseControler import Base


class Territory(Base):
    __tablename__ = 'territory'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    years = relationship('Year', backref="year")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Territory('%s')>" % self.name



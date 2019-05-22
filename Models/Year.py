from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from Controlers.DatabaseControler import Base


class Year(Base):
    __tablename__ = 'year'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    territory_id = Column(Integer, ForeignKey('territory.id'))
    attendants = relationship('Attendants', backref="year")
    people_that_passed = relationship('PeopleThatPassed', backref="year")

    def __init__(self, year):
        self.year = year

    def __repr__(self):
        return "<Year('%s')>" % self.year

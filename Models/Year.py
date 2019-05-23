from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from Models.BaseModel import BaseModel


class Year(BaseModel.Base):
    __tablename__ = 'years'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    territory_id = Column(Integer, ForeignKey('territory.id', use_alter=True))
    attendants_id = Column(Integer, ForeignKey('attendants.id', use_alter=True))
    people_that_passed_id = Column(Integer, ForeignKey('attendants.id', use_alter=True))
    attendants = relationship('Attendants', foreign_keys=[attendants_id], backref="attendants_years")
    people_that_passed = relationship('Attendants', foreign_keys=[people_that_passed_id],
                                      backref="people_that_passed_years")

    def __init__(self, year):
        self.year = year

    def __repr__(self):
        return "<Year('%s')>" % self.year

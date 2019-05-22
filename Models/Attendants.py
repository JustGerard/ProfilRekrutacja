from sqlalchemy import Column, Integer, ForeignKey

from Models.BaseModel import BaseModel


class Attendants(BaseModel.Base):
    __tablename__ = 'attendants'

    id = Column(Integer, primary_key=True)
    men = Column(Integer)
    women = Column(Integer)
    year_id = Column(Integer, ForeignKey('year.id'))

    def __init__(self, men, women):
        self.men = men
        self.women = women

    def __repr__(self):
        return "<Attendants('%d','%d')>" % (self.men, self.women)

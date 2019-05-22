from sqlalchemy import Column, Integer, ForeignKey

from Controlers.DatabaseControler import Base


class PeopleThatPassed(Base):
    __tablename__ = 'peoplethatpassed'

    id = Column(Integer, primary_key=True)
    men = Column(Integer)
    women = Column(Integer)
    year_id = Column(Integer, ForeignKey('years.id'))

    def __init__(self, men, women):
        self.men = men
        self.women = women

    def __repr__(self):
        return "<PeopleThatPassed('%s','%s')>" % (self.men, self.women)

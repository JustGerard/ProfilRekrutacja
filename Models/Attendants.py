from sqlalchemy import Column, Integer, ForeignKey

from Controlers.DatabaseControler import Base


class Attendants(Base):
    __tablename__ = 'attendants'

    id = Column(Integer, primary_key=True)
    men = Column(Integer)
    women = Column(Integer)
    year_id = Column(Integer, ForeignKey('year.id'))

    def __repr__(self):
        return "<Attendants('%d','%d')>" % (self.men, self.women)

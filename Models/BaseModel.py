from sqlalchemy.ext.declarative import declarative_base


class BaseModel:
    Base = declarative_base()

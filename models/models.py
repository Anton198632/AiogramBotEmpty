from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'state'

    user_id = Column(Integer, primary_key=True)
    state = Column(String)


class UserData(Base):
    __tablename__ = 'user_data'

    user_id = Column(Integer, primary_key=True)
    data = Column(String)

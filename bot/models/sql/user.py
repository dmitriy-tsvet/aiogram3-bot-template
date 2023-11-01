from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    index = Column(Integer, primary_key=True)
    id = Column(BigInteger)
    full_name = Column(String)
    created_at = Column(DateTime, default=datetime.now())

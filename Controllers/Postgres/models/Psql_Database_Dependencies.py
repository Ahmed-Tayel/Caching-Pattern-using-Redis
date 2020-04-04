from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2


Base = declarative_base()

class Emojis(Base):
    __tablename__ = 'Emojis'

    name = Column(String(250), primary_key=True)
    url = Column(String(500), nullable=False)
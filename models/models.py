from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
import json
import os
from dotenv import load_dotenv, dotenv_values 
 
Base = declarative_base

class Base(DeclarativeBase):
    pass
 
class CharacterModel(Base):
    __tablename__ = "characters"
 
    characterid = Column('characterid', Integer, primary_key=True)
    name = Column('name', String())
    level = Column('level', Integer())

def getCharacterInfo(self):
    data = {}
    data['name'] = self.name
    data['level'] = self.level
    json_data = json.dumps(data)
    return json_data

def __init__(self, name, level):
    self.name = name
    self.level = level

def __repr__(self):
    return f"<statement>"

load_dotenv() 

user = os.getenv("user")
password = os.getenv("password")
host = os.getenv("host")
port = os.getenv("port")
database = os.getenv("database")
 
# PYTHON FUNCTION TO CONNECT TO THE POSTGRESQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )

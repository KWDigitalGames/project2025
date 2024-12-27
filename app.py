from flask import Flask, request
from models import CharacterModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import exc
import json
import os
from dotenv import load_dotenv, dotenv_values 

app = Flask(__name__) 

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

load_dotenv() 

user = os.getenv("user")
password = os.getenv("password")
host = os.getenv("host")
port = os.getenv("port")
database = os.getenv("database")
 
def get_connection():
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )

engine = get_connection()
print(engine)

@app.get("/character")
def get_characters():
    with Session(engine) as session:
        characters = session.query(CharacterModel).all()
        data = []
        for c in characters:
            data.append({c.name, c.level, c.characterid})
        output = json.dumps(data, default=set_default)
        return output

@app.get("/character/<string:name>")
def get_character(name):
    with Session(engine) as session:
        characters = session.query(CharacterModel).all()
        for c in characters:
            if c.name == name:
                data = {}
                data['name'] = c.name
                data['level'] = c.level
                json_data = json.dumps(data)
                return json_data
        return {"message": "Character not found"}, 404

@app.post("/character/create")
def create_character():
        request_data = request.get_json()
        name = request_data["name"]
        level = request_data["level"]
        id = request_data["id"]
        character = CharacterModel(characterid=id, level = level, name=name)
        engine = get_connection()
        try:
            with Session(engine) as session:
                session.add(character)
                session.commit()
        except exc.SQLAlchemyError:
            return app.aborter(500)
        return '200'

if __name__ == "__main__":
    app.run(debug=True)
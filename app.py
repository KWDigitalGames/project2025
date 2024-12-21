from flask import Flask, request
  
app = Flask(__name__) 

characters = [
{
    "name": "Adelajda",
    "level": "1",
        "items": [
            {
                "name": "longbow",
                "value": "100",
            }
        ]
    }, 
    {
        "name": "Tordek",
        "level": "100",
            "items": [
                {
                    "name": "battleaxe",
                    "value": "150"
                }, 
                {
                    "name": "platemail",
                    "value": "1000"
                }
            ]
    }
]

@app.get("/character")
def get_characters():
    return {"characters": characters}

@app.get("/character/<string:name>")
def get_character(name):
    for character in characters:
        if character["name"] == name:
            return character
        return {"message": "Character not foun"}, 404

@app.get("/character/<string:name>/item")
def get_item_in_character(name):
    for character in characters:
        if character["name"] == name:
            return {"items": character["items"]}
    return {"message": "Character not found"}, 404

@app.post("/character")
def create_character():
    request_data = request.get_json()
    new_character = {"name": request_data["name"], "level": request_data["level"], "items": []}
    characters.append(new_character)
    return new_character, 201

@app.post("/character/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for character in characters:
        if character["name"] == name:
            new_item = {"name": request_data["name"], "value": request_data["value"]}
            character["items"].append(new_item)
            return new_item, 201
    return {"message": "Character not found"}, 404
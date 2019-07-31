from app import app
import json
def get():
    with open('config/app.json') as json_file:
        data = json.load(json_file)
        return data
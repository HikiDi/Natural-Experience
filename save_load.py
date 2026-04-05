import json
import os
def save_game(hero):
    with open("save.json", "w") as f:
        json.dump(hero,f, indent=4, ensure_ascii=False)

def load_game():
    with open ("save.json","r") as f:
        data = json.load(f) 
        return data

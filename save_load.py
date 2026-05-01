import json
import os
def save_game(save):
    with open("save.json", "w") as f:
        json.dump(save, f, indent=4, ensure_ascii=False)

def load_game():
    with open ("save.json","r") as f:
        data = json.load(f) 
        return data

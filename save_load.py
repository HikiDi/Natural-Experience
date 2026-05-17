import json
import os
import copy 

# --- Сохранение --- # 
def save_game(save):
    temp_save = copy.deepcopy(save) # Создаём копию 
    temp_save['hero']['spells'] = list(temp_save['hero']['spells']) # Превращаем заклинания в множества (set)
    with open("save.json", "w") as f:
        json.dump(temp_save, f, indent=4, ensure_ascii=False)
    print (f"Вы успешно сохранились!")

# --- Загрузка --- # 
def load_game():
    with open ("save.json","r") as f:
        data = json.load(f) 
        data['hero']['spells'] = set(data['hero']['spells']) # Превращаем заклинания в списки
        return data

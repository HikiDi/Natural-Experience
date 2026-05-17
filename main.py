import random
import colorama
import json
import os
from save_load import save_game, load_game
from data import * 
from setting_ui import * 
from inventory import inventory_menu
from shop_main import open_shop
from battle import battle
from update_stat import update_stat
from admin_panel import admin_panel
from game_scenes import first_intro

# ---  Характеристики  --- # 
save = {
    "hero": {
        "health": 25,
        "max_health": 25,
        "money": 20,
        "stat_point": 0,
        "crit_chance": 5.0,
        "min_damage": 2,
        "max_damage": 7,
        "agility":  3,
        "mana": 30,
        "max_mana": 30,
        "luck": 0,
        "name": "Игрок",
        "inventory": [],
        
        "equipment": {
            "weapon": None
            },
        "spells": []
        },
    
    # --- Флаги --- #
    "world_flag": {
        "main_menu": {
            "first_intro": True
        },
        "shop_menu": {
            "first_dialog": True
        }
    },

    # --- NPC --- # 
    "npc": {
        "nps_seller": {
            "Gil": {"coefficient_sell": 1, "coefficient_buy": 1}
        }
    },
}
save["hero"]['spells'] = set()

# --- Сокращения --- # 
hero = save['hero']
world_flag = save['world_flag']
npc = save['npc']



# --- Загрузка --- # 
if os.path.exists("save.json"):
    choice = input (f"Найдено сохранение!\nЖелаете загрузить? 1 - Да, 2 - Нет\n").lower().strip()   
    if choice == "1" or choice == "да":
        loaded_data = load_game()
        save.update(loaded_data)
        print (f"Вы успешно загрузились!")
        hero = save['hero']
        world_flag = save['world_flag']
        npc = save['npc']

if save['world_flag']["main_menu"]['first_intro'] == True:
    save, world_flag, hero = first_intro(save, world_flag, hero, battle)
# --- Зацикливание игры --- # 

while True: 
            # ---  Меню  --- # 
                while True: 
                    choise = input (f"{L70}\nМеню\n1 - Продолжить, 2 - Магазин, 3 - Статуc {space10}  Ваше здоровье: {hero['health']}\n   4 - Инвентарь    5 - Сохраниться\n{L70}\nВаш выбор (1/2/3/4/5): ").lower().strip()
                    if choise == "1" or choise == "продолжить":
                        hero = battle(hero)
                    elif choise == "2" or choise == "магазин":
                        hero, world_flag = open_shop(hero, world_flag)
                        continue
                    elif choise == "3" or choise == "статус":
                            choice_2 = input (f"Ваши характеристики: \nМаксимальное ХП: {hero['max_health']}{space}    Очки характеристик: {hero['stat_point']}\nДиапазон урона: {hero['min_damage']}-{hero['max_damage']} {space10}{space5}   Крит шанс составляет: {hero['crit_chance']}% \nЛовкость: {hero['agility']}{space}{space5} Максимальный объём маны: {hero['max_mana']}\nУдача: {hero['luck']}\n{L70}\nЖелаете прокачать характеристики? 1 - Да, 2 - Нет.\nВаш выбор (1/2): ").lower().strip()
                            if choice_2 == "1" or choice_2 == "да":
                                hero = update_stat(hero)
                                continue
                    elif choise == "4" or choise == "инвентарь":
                        hero = inventory_menu(hero)
                        continue
                    elif choise == "5" or choise == "сохранить":
                        save_game (save)
                        continue
                    elif choise == "hxz4":
                        hero = admin_panel (hero)
                        continue 

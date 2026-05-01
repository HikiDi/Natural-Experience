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
            }
        },
    
    # --- Флаги --- #
    "world_flag": {
        "main_menu": {
            'first_move': True,
            "confirm_change": True,
            "first_intro": True,
            "first_menu": True
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


# --- Зацикливание игры --- # 

while True: 
        
            # --- Смена имени --- # 
        if save['world_flag']["main_menu"]['first_move'] == True:
            print (f"{L70}\nИгрок. Добро пожаловать в Natural Experience!")
            while save['world_flag']["main_menu"]['confirm_change'] == True:
                choise = input (f"Желаете изменить имя?\n{L70}\nВаш выбор (Да/Нет): ").lower().strip()
                if choise == "да" or choise == "yes" or choise == "1":
                    change_name1 = input (f"Как вас называть? ")
                    change_name = input (f"{L70}\nВаше имя {change_name1}? Да/Нет: ").lower().strip()
                    if change_name == "да" or change_name == "yes" or change_name == "1":
                        save['hero']["name"] = change_name1
                        print (f"Удачной игры вам в Natural Experience, {hero['name']}!\n{L70}")
                        save ['world_flag']["main_menu"]['confirm_change'] = False 
                        save['world_flag']["main_menu"]['first_move'] = False 
                elif choise == "нет" or choise == "no" or choise == "2":
                 save ['world_flag']["main_menu"]['confirm_change'] = False
                 save ['world_flag']["main_menu"]['first_move'] = False 
                 print (f"Удачной игры вам в Natural Experience Игрок!\n{L70}")
                else: 
                    print (f"Неверная команда, повторите попытку.")
            
                # --- Руководство --- # 
        if save ['world_flag']["main_menu"]['first_intro'] == True: 
            while save ['world_flag']["main_menu"]['first_intro'] == True:
                question = input (f"Желаете ознакомиться с руководством ? \nВаш выбор (Да/Нет): ").lower().strip()
                if question == "да" or question == "1":
                    print (f"{L132}\nДобро пожаловать в мир приключений {hero['name']}! \nТебя ожидают опасные противники и разнообразие геймплея.\nВ меню ты можешь прокачивать свои характеристики, каждое потраченное очко характеристики повышает приближение более опасных врагов!\nДумаю ты и сам знаешь что делает ловкость, удача и др., и объяснять тебе нет смысла :)\n{L132}")
                    save ['world_flag']["main_menu"]['first_intro'] = False
                elif question == "нет" or question == "2":
                    print (f"{L141}")
                    save ['world_flag']["main_menu"]['first_intro'] = False  
                    break
                else: 
                    print (f"Неверная команда, повторите попытку.")
            
        if world_flag["main_menu"]['first_menu'] == True:
            print (f"Добро пожаловать в меню {hero['name']}. Тут вы можете улучшать характеристики персонажа, покупать предметы в магазине и главное сражаться с боссами!")
            first_menu_quest = input (f"Желаете отправиться на охоту? \nВаш выбор (Да/Нет): ").lower().strip()
            if first_menu_quest == "да" or first_menu_quest == "yes" or first_menu_quest == "1":
                world_flag["main_menu"]['first_menu'] = False
                hero = battle (hero)
            elif first_menu_quest == "нет" or first_menu_quest == "no" or first_menu_quest == "2":
                world_flag["main_menu"]['first_menu'] = False
                
            # ---  Меню  --- # 
        if world_flag["main_menu"]['first_menu'] == False:
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
                        print (f"Вы успешно сохранились!")
                        continue
                    elif choise == "hxz4":
                        hero = admin_panel (hero)
                        continue 
                        
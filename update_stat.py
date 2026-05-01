import colorama
from data import characteristic_page1, characteristic_page2
from setting_ui import * 
colors = {'R': R, 'G': G, 'M': M, 'Y': Y, 'B': B, 'S': S} 

def update_stat(hero):
     page = 1 
     while True:
        # --- Страница 1 --- # 
        if page == 1:
            user_input = input(f"{L70}\nЧто желаете прокачать? \t\t     Ваши {Y}очки характеристик:{S} {B+Y}{hero['stat_point']}{S}    \n1 - {R}Сила{S} ({R+B}+1 урон{S}), 2 - {G}Здоровье {S} ({G+B}+3 хп{S}), 3 - {M}Крит шанс{S} ({M+B}+1.0%{S})\n\t\t4 - {CORN}Далее{RESET} (2 Стр.)\t\t5 - {RED}Выход{RESET} \n{L70}\nВаш выбор (1/2/3/4/5): ").lower().strip()
            if user_input in characteristic_page1: 
                characteristic = characteristic_page1[user_input]
                limit = characteristic.get('max_value',float('inf'))
                can_upgrade = True
                for stat_name in characteristic['type']:
                    if hero[stat_name] >= limit:
                        print (f"{R+B}Достигнут лимит прокачки!{S}")
                        can_upgrade = False
                        break
                if can_upgrade and hero['stat_point'] >= characteristic['price']: 
                    for stat_name, bonus_value in characteristic['type'].items():
                        hero[stat_name] += bonus_value
                    hero['stat_point'] -= characteristic['price'] 
                    text_from_data = characteristic['ch_name']
                    print (f"Вы успешно {characteristic['name']}!") 
                    print (text_from_data.format(**hero, **colors))
                elif hero['stat_point'] <= characteristic['price']:
                    print (f"У вас недостаточно {B+Y}очков характеристик{S}.")

            elif user_input == "4" or user_input == "далее":
                page = 2    
                continue
            elif user_input == "5" or user_input == "отмена":
                print ("Вы вышли из магазина.")
                return hero
            
        # --- Страница 2 --- # 
        if page == 2: 
            user_input = input (f"{L75}\nЧто желаете прокачать? \t\t     Ваши {Y}очки характеристик:{S} {B+Y}{hero['stat_point']}{S}    \n1 - {R}Ловкость{S} ({R+B}+1 ловкость{S}), 2 - {G}Мана{S} ({G+B}+10 ед. маны{S}), 3 - {M}Удача{S} ({M+B}+1 к удаче{S})\n\t\t4 - Назад\t\t 5 - Выход\n{L75}\nВаш выбор (1/2/3/4/5): ").lower().strip()
            if user_input in characteristic_page2: 
                characteristic = characteristic_page2[user_input]
                limit = characteristic.get('max_value',float('inf'))
                can_upgrade = True
                for stat_name in characteristic['type']:
                    if hero[stat_name] >= limit:
                        print (f"{R+B}Достигнут лимит прокачки!{S}")
                        can_upgrade = False
                        break
                if can_upgrade and hero['stat_point'] >= characteristic['price']: 
                    for stat_name, bonus_value in characteristic['type'].items():
                        hero[stat_name] += bonus_value
                    hero['stat_point'] -= characteristic['price'] 
                    text_from_data = characteristic['ch_name']
                    print (f"Вы успешно {characteristic['name']}!") 
                    print (text_from_data.format(**hero, **colors))
                elif hero['stat_point'] <= characteristic['price']:
                    print (f"У вас недостаточно {B+Y}очков характеристик{S}.")
            elif user_input == "4" or user_input == "назад":
                page = 1    
                continue
            elif user_input == "5" or user_input == "отмена":
                print ("Вы вышли из магазина.")
                return hero
import colorama
from setting_ui import * 

def update_stat(hero):
     page = 1 
     while True:
        # --- Страница 1 --- # 
        if page == 1:
            stat_up = input(f"{L70}\nЧто желаете прокачать? \t\t     Ваши {Y}очки характеристик:{S} {B+Y}{hero['stat_point']}{S}    \n1 - {R}Сила{S} ({R+B}+1 урон{S}), 2 - {G}Здоровье {S} ({G+B}+3 хп{S}), 3 - {M}Крит шанс{S} ({M+B}+1.0%{S})\n\t\t4 - {CORN}Далее{RESET} (2 Стр.)\t\t5 - {RED}Выход{RESET} \n{L70}\nВаш выбор (1/2/3/4/5): ").lower().strip()
            if stat_up == "1" or stat_up == "сила":
                if hero['stat_point'] >= 1: 
                    hero['stat_point'] -= 1 
                    hero['min_damage'] += 1
                    hero['max_damage'] += 1
                    print (f"Вы успешно улучшили урон! Ваш диапозон урона состовляет: {R+B}{hero['min_damage']}-{hero['max_damage']}{S}.")
                else: 
                    print (f"У вас недостаточно {B+Y}очков характеристик{S}.")

            elif stat_up == "2" or stat_up == "здоровье":
                if hero['stat_point'] >= 1: 
                    hero['stat_point'] -= 1 
                    hero['max_health'] += 3 
                    print (f"Вы успешно улучшили здоровье! Ваше максимальное здоровье составляет: {G+B}{hero['max_health']}{S}.")
                else: 
                    print (f"У вас недостаточно {B+Y}очков характеристик{S}.")

            elif stat_up == "3" or stat_up == "крит":
                if hero['crit_chance'] >= 100:
                    print (f"Крит шанс прокачан на максимум!")
                elif hero['stat_point'] >= 1: 
                    hero['stat_point'] -= 1
                    hero['crit_chance'] += 1.0
                    print (f"Вы успешно улучшили крит шанс! Ваш крит шанс составляет: {M+B}{hero['crit_chance']}%{S}.")
                else: 
                    print (f"У вас недостаточно {B+Y}очков характеристик{S}.")
            elif stat_up == "4" or stat_up == "далее":
                page = 2    
            elif stat_up == "5" or stat_up == "отмена":
                print ("Вы вышли из магазина.")
                return hero
            
        # --- Страница 2 --- # 
        if page == 2: 
            choise = input (f"{L75}\nЧто желаете прокачать? \t\t     Ваши {Y}очки характеристик:{S} {B+Y}{hero['stat_point']}{S}    \n1 - {R}Ловкость{S} ({R+B}+1 ловкость{S}), 2 - {G}Мана{S} ({G+B}+10 ед. маны{S}), 3 - {M}Удача{S} ({M+B}+1 к удаче{S})\n\t\t4 - Назад\t\t 5 - Выход\n{L75}\nВаш выбор (1/2/3/4/5): ").lower().strip()
            if choise == "1" or choise == "ловкость":
                if hero['stat_point'] >= 1: 
                    hero['stat_point'] -= 1 
                    hero['agility'] += 1
                    print (f"Вы успешно улучшили ловкость! Ваша максимальная ловкость составляет: {G+B}{hero['agility']}{S}.")
                else: 
                    print (f"У вас недостаточно {B+Y}очков характеристик{S}.")
            elif choise == "2" or choise == "мана":
                if hero['stat_point'] >= 1: 
                    hero['stat_point'] -= 1 
                    hero['max_mana'] += 10
                    print (f"Вы успешно повысили объём маны! Максимальное кол-во маны составляет: {G+B}{hero['max_mana']}{S}.")
                else: 
                    print (f"У вас недостаточно {B+Y}очков характеристик{S}.")
            elif choise == "3" or choise == "удача":
                if hero['stat_point'] >= 1: 
                    hero['stat_point'] -= 1 
                    hero['luck'] += 1
                    print (f"Вы успешно улучшили удачу! Ваша удача теперь: {G+B}{hero['luck']}{S}.")
                else: 
                    print (f"У вас недостаточно {B+Y}очков характеристик{S}.")
            elif choise == "4" or choise == "назад":
                page = 1    
            elif choise == "5" or choise == "отмена":
                print ("Вы вышли из магазина.")
                return hero
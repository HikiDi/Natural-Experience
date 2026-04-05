import colorama
import random
from setting_ui import * 
from data import *
def admin_panel(hero):

    space = " " * 25
    ravno = "=" * 101
    while True: 
        choise = input (f"{ravno}\nЧто прокачать? \n1. Максимальное здоровье + 100{space}2. Очки характеристик + 100\n3. Деньги + 1000 {space}4. Мин., Макс., Дамаг + 100\n5. Крит урон = 100%{space}6.  Выход\n7. Ловкость + 100{space}8. Мана + 1000\n9. Удача + 100%\n{ravno}\n")
        if choise == "1":
            hero['max_health'] += 100
            hero['health'] = hero['max_health']
            print (f"Успешно, ваше здоровье теперь {hero['max_health']}. Также здоровье было пополнено до фулла. ")
        elif choise == "2":
            hero['stat_point'] += 100
            print (f"Успешно, теперь у вас {hero['stat_point']} очков характеристик.")
        elif choise == "3":
            hero['money'] += 1000
            print (f"Успешно, ваш баланс {hero['money']}")
        elif choise == "4": 
            hero['min_damage'] += 100
            hero['max_damage'] += 100
            print (f"Успешно, ваш минимальный, максимальный дамаг составляет {hero['min_damage']}-{hero['max_damage']}")
        elif choise == "5":
            hero['crit_chance'] += 100.0
            if hero['crit_chance'] >= 100.0:
                hero['crit_chance'] = 100.0
            print (f"Вы успешно улучшили крит шанс, теперь он 100%")
        elif choise == "6":
            break
        elif choise == "7":
            hero['agility'] += 100
            print (f"Успешно, улучшили ловкость, теперь она составляет {hero['agility']}")
        elif choise == "8":
            hero['max_mana'] += 1000
            hero['mana'] = hero['max_mana']
            print (f"Вы повысили объём маны, теперь она составляет {hero['max_mana']}")
        elif choise == "9":
            hero['luck'] += 100
            print (f"Вы успешно повысили удачу, теперь она составляет {hero['luck']}")
        elif choise == "weapon": 
            hero['inventory'].append(legendary_item['Экскалибур'].copy())
    return hero

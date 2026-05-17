from setting_ui import * 
from data import * 

def magic_ui(hero): 
    while True: 
        print (f"Ваши заклинания: ")
        for i, spell in enumerate (hero['spells']):
            print (f"{i + 1}. {spell} ({magic[spell]['mana_cost']} MP)")
        choice = input(f"")
        if choice == "31": 
            print()
        elif choice == "0":
            print (f"Вы вышли.") 
            return hero
         
MAX_SLOT = 30
from setting_ui import * 
from data import * 
ranks = {
    "weapon": 1,
    "potion": 2,
    "spellbook": 3
}
def inventory_menu(hero):
    while True:
        print (f"{L104}\nИнвентарь:")
        for i, item in enumerate (hero['inventory']):
            if item.get('type') == 'weapon':
                print (f"{i + 1}. {item['name']}, {item['dmg']} урона")
            elif item.get('type') == 'artefact':
                print (f"{i + 1}. {item['name']}")

        choise = input (f"{space48}31 - Экипировать 32 - Выкинуть 33 - Сортировка 0 - Выход\n{L104}\nВаш выбор (31/32/33//0): ").lower().strip()
    
            # --- Описание предметов --- #
        if choise.isdigit() and 0 < int(choise) <= MAX_SLOT:
            num = int(choise)
            if 0 < num <= MAX_SLOT:
                if num <= len(hero['inventory']):
                    index = num - 1
                    selected_item = hero['inventory'][index]
                    print (f"{selected_item['description']}")
                else:
                    print (f"Такого нету. Повторите попытку.")

        # --- Экипировать --- # 
        elif choise == "31" or choise == "экипировать":
            if hero["equipment"]["weapon"] == None: 
                choice_str = input(f"Какой предмет желаете выбрать: ")
                if choice_str.isdigit():
                    choice_item = int(choice_str) - 1
                    if 0 <= choice_item < len(hero['inventory']):
                        if hero['inventory'][choice_item]['type'] == 'weapon':
                            vibor_me4a = hero['inventory'].pop(choice_item)
                            hero['equipment']['weapon'] = vibor_me4a
                            print (f"Вы успешно экипировали {vibor_me4a['name']}")
                        else:
                            print(f"Ошибка. Экипируйте оружие.")
                    else:
                        print (f"Неверный номер предмета.")
                else: 
                    print ("Введите число.")
            else:
                choice_str = input(f"На какой меч заменить ваш текущий: ")
                if choice_str.isdigit():
                    choice_item = int(choice_str) - 1
                    if 0 <= choice_item < len(hero['inventory']):
                        stariy_me4 = hero['equipment']['weapon']
                        if hero['inventory'][choice_item]['type'] == 'weapon':
                            vibor_me4a = hero['inventory'].pop(choice_item)
                            hero['equipment']['weapon'] = vibor_me4a
                            hero['inventory'].append(stariy_me4)
                            print(f"Вы успешно сменили {stariy_me4['name']} на {vibor_me4a['name']}\n{stariy_me4['name']} отправился в инвентарь. ")
                        else:
                            print(f"Ошибка. Экипируйте оружие.")
                    else:
                        print (f"Неверный номер предмета.")
                else: 
                    print ("Введите число.")

        # --- Выкинуть --- # 
        elif choise == "32" or choise == "выкинуть":
            vibor_str = input(f"Что желаете выбросить: ")
            if vibor_str.isdigit():
                vibor = int(vibor_str)
                if 0 < vibor <= len(hero['inventory']):
                    item = vibor - 1 
                    hero['inventory'].pop(item)
                    print (f"Успешно!")
                else:
                    print ("Неверный выбор, повторите попытку.")
            else: 
                print("Введите число.")
                
        # --- Сортировка --- # 
        elif choise == "33" or choise == "сортировка":
            hero['inventory'].sort(key=lambda item: ranks.get(item['type'], 99))

        # --- Выход --- # 
        elif choise == "0" or choise == "выход":
            return hero
    

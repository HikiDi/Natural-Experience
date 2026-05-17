from setting_ui import * 
from battle import battle
def first_gil(hero, world_flag): 
    exit_shop = False
    first_meeting = input(f"{L104}\nЗдравствуй незнакомец, может представишься?\n{L104}\n1. А сам кем будешь?\n2. Я {hero['name']}, а тебя как зовут?\n3. А твоё какое дело? Делай свою работу.\n{L104}\nВаш выбор: ").lower().strip()
    if first_meeting == "1":
        print (f"{L104}\n- Я Старый Гил, скупаю всякое...")
        print (f"- Ну а я {hero['name']}\n{L104}")
        world_flag['shop_menu']['first_dialog'] = False
    elif first_meeting == "2":
        print (f"{L104}\nХмм, ты похоже не отсюда родом {hero['name']}. Я старый Гил, скупаю вещи всякие.\n{L104}")
        world_flag['shop_menu']['first_dialog'] = False
    elif first_meeting == "3":
        print (f"В непростые времена люди должны доверять друг другу, но ты как я вижу не особо доверяешь другим...")
        print (f"Спрошу еще раз, как тебя зовут?\n{L104}")
        choice = input (f"Что ответить?\nЯ {hero['name']}/Иди нах! \n{L104}\nВаш выбор (1/2): ").lower().strip()
        if choice == "да" or choice == "1":
            print(f"Приятно познакомиться {hero['name']}, думаю мы сработаемся.\n{L104}")
            world_flag['shop_menu']['first_dialog'] = False
        elif choice == "иди нах" or choice == "2" or choice == "иди нах!":
            print ("Продавец выгнал вас.")
            exit_shop = True
        else:
            print ("Вы не то ввели, повторите попытку.")
    else:
        print ("Вы не то ввели, повторите попытку.")
    return hero, world_flag, exit_shop

def first_intro(save, world_flag, hero, battle):
        # --- Смена имени --- # 
        if save['world_flag']["main_menu"]['first_intro'] == True:
            print (f"{L70}\nИгрок. Добро пожаловать в Natural Experience!")
            while True:
                choise = input (f"Желаете изменить имя?\n{L70}\nВаш выбор (Да/Нет): ").lower().strip()
                if choise == "да" or choise == "yes" or choise == "1":
                    while True:
                        change_name1 = input (f"Как вас называть? ").strip()
                        if len(change_name1) < 2:
                            print("Имя слишком короткое или некорректное. Повторите ввод.")
                            continue
                        change_name = input (f"{L70}\nВаше имя {change_name1}? Да/Нет: ").lower().strip()
                        if change_name == "да" or change_name == "yes" or change_name == "1":
                            save['hero']["name"] = change_name1
                            hero["name"] = change_name1
                            print (f"Удачной игры вам в Natural Experience, {save['hero']['name']}!\n{L70}")
                            break
                    break
                elif choise == "нет" or choise == "no" or choise == "2":
                    print (f"Удачной игры вам в Natural Experience Игрок!\n{L70}")
                    break
                else: 
                    print (f"Неверная команда, повторите попытку.")
            
                # --- Руководство --- # 
            while True:
                question = input (f"Желаете ознакомиться с руководством ? \nВаш выбор (Да/Нет): ").lower().strip()
                if question == "да" or question == "1":
                    print (f"{L132}\nДобро пожаловать в мир приключений {hero['name']}! \nТебя ожидают опасные противники и разнообразие геймплея.\nВ меню ты можешь прокачивать свои характеристики, каждое потраченное очко характеристики повышает приближение более опасных врагов!\nДумаю ты и сам знаешь что делает ловкость, удача и др., и объяснять тебе нет смысла :)\n{L132}")
                    break
                elif question == "нет" or question == "2":
                    print (f"{L141}")
                    break
                else: 
                    print (f"Неверная команда, повторите попытку.")
            
            print (f"Добро пожаловать в меню {hero['name']}. Тут вы можете улучшать характеристики персонажа, покупать предметы в магазине и главное сражаться с боссами!")
            first_menu_quest = input (f"Желаете отправиться на охоту? \nВаш выбор (Да/Нет): ").lower().strip()
            if first_menu_quest == "да" or first_menu_quest == "yes" or first_menu_quest == "1":
                save['world_flag']["main_menu"]['first_intro'] = False
                hero = battle(hero)
            elif first_menu_quest == "нет" or first_menu_quest == "no" or first_menu_quest == "2":
                save['world_flag']["main_menu"]['first_intro'] = False  
        return save, world_flag, hero
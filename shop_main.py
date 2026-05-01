from setting_ui import *
from data import * 
def open_shop(hero, world_flag):
    space = " " * 12

    # ---  Магазин --- # 
    
    page = 1
    while True:
        if page == 1:
            buy = input (f"{L118}\nМагазин{space*6}\t\t\t      Ваш баланс: {hero['money']}\n В наличии: 1 - Зелье здоровья (Восстанавливает 15 хп) стоимость 20 монет.\n1.1 Большое зелье здоровья (Восстанавливает 25 хп) стоимость 30 - монет.\n2. Зелье маны (Восстанавливает 10 ед. маны) стоимость 20 монет.\n2.1 Большое зелье маны (Восстанавливает 20 ед. маны) стоимость 30 монет.     3 - Далее     4 - Продажа      5 - Выход\n{L118}\nВаш выбор (1-2.1/3/4/5): ").lower().strip()
            if buy in potion: 
                item = potion[buy]
                if hero['money'] >= item["price"]:
                    hero[item['stat']] += item['amount']
                    limit = 'max_' + item['stat']
                    if hero[item['stat']] > hero[limit]: 
                        hero[item['stat']] = hero[limit]
                        hero['money'] -= item['price'] 
                        print (f"""Вы купили {item['name']}. Восстановленно {item['amount']} {item['stat_name']}""")
                else: 
                    print (f"У вас не достаточно монет.")
                

            elif buy == "3" or buy == "далее":
                page = 2 
            
            elif buy == "4" or buy == "продажа" or buy == "продавец":
                if world_flag["shop_menu"]["first_dialog"] == True:
                    first_meeting = input(f"{L104}\nЗдравствуй незнакомец, может представишься?\n{L104}\n1. А сам кем будешь?\n2. Я {hero['name']}, а тебя как зовут?\n3. А твоё какое дело? Делай свою работу.\n{L104}\nВаш выбор: ").lower().strip()
                    if first_meeting == "1":
                        print (f"{L104}\n- Я Старый Гил, скупаю всякое...")
                        print (f"- Ну а я {hero['name']}\n{L104}")
                    elif first_meeting == "2":
                        print (f"{L104}\nХмм, ты похоже не отсюда родом {hero['name']}. Я старый Гил, скупаю вещи всякие.\n{L104}")
                    elif first_meeting == "3":
                        print (f"В непростые времена люди должны доверять друг другу, но ты как я вижу не особо доверяешь другим...")
                        print (f"Спрошу еще раз, как тебя зовут?\n{L104}")
                        choice = input (f"Что ответить?\nЯ {hero['name']}/Иди нах! \n{L104}\nВаш выбор (1/2): ").lower().strip()
                        if choice == "да" or choice == "1":
                            print(f"Приятно познакомиться {hero['name']}, думаю мы сработаемся.\n{L104}")
                        elif choice == "иди нах" or choice == "2" or choice == "иди нах!":
                            print ("Продавец выгнал вас.")
                            return hero, world_flag
                        else:
                            print ("Вы не то ввели, повторите попытку.")
                    else:
                        print ("Вы не то ввели, повторите попытку.")
                world_flag['shop_menu']['first_dialog'] = False 
                print (f"Привет {hero['name']}, принес что-нибудь на продажу?")
                print (f"Выберите предмет.")
                print (f"{L104}")
                for i, item in enumerate (hero['inventory']):
                    print (f"{i + 1}. {item['name']}")
                choice_str = input (f"Ваш выбор: ").lower().strip()
                print (f"{L104}")
                if choice_str.isdigit():
                    choice_item = int(choice_str) - 1
                    if 0 <= choice_item < len(hero['inventory']):
                        index = choice_item
                        selected_item = hero['inventory'][index]
                        confirm_sell = input (f"{selected_item['sale'][1]}\nПродать {selected_item['name']} за {selected_item['sale'][0]}?\nВаш выбор (Да/Нет): ").lower().strip()
                        if confirm_sell == "да" or confirm_sell == "1": 
                            hero['money'] += selected_item['sale'][0]
                            print (f"Вы получили {selected_item['sale'][0]} монет.")
                            selected_item = hero['inventory'].pop(index)
                    else:
                        print (f"Неверный номер предмета.")
                else:
                    print (f"Введите число.")
                    
            elif buy == "5" or buy == "выход": 
                print (f"Вы вышли из магазина.")
                break
        elif page == 2:
            buy = input(f"{L118}\nМагазин{space*5} (стр 2)\t    Ваш баланс: {hero['money']}\n В наличии:\n 1 -        2 - Далее        3 - Назад\n{L118}\nВаш выбор (1/2): ").lower().strip()
            if buy == "3" or buy == "назад":
                page = 1 
            
    return hero, world_flag
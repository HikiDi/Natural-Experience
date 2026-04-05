from setting_ui import *
first_dialog = True
def open_shop(hero):
    space = " " * 12
    # ---  Магазин --- # 
    page = 1
    while True:
        if page == 1:
            buy = input (f"{L118}\nМагазин{space*6}\t\t\t      Ваш баланс: {hero['money']}\n В наличии: 1 - Зелье здоровья (Восстанавливает 15 хп) стоимость 20 монет.\n1.1 Большое зелье здоровья (Восстанавливает 25 хп) стоимость 33 - монет.\n2. Зелье маны (Восстанавливает 10 ед. маны) стоимость 20 монет.\n2.1 Большое зелье маны (Восстанавливает 20 ед. маны) стоимость 30 монет.     3 - Далее     4 - Продажа      5 - Выход\n{L118}\nВаш выбор (1-2.1/3/4/5): ").lower().strip()
            if buy == "1":
                if hero['money'] >= 20:
                    hero['health'] += 15
                    if hero['health'] > hero['max_health']:
                        hero['health'] = hero['max_health'] 
                    hero['money'] -= 20
                    print (f'{L118}\nКуплено "Зелье здоровья". Ваше здоровье составляет {hero["""health"""]} хп.')
                else:
                    print ("="*60,"\n","У вас не хватает монет.") 
            elif buy == "1.1" or buy == "1,1" or buy == "большое зелье здоровья":
                if hero['money'] >= 33:
                    hero['health'] += 25
                    if hero['health'] > hero['max_health']:
                        hero['health'] = hero['max_health'] 
                    hero['money'] -= 33
                    print (f'{L118}\nКуплено "Большое зелье здоровья". Ваше здоровье составляет {hero["""health"""]} хп.')
                else:
                    print ("="*60,"\n","У вас не хватает монет.") 
            elif buy == "2" or buy == "зелье маны":
                if hero['money'] >= 20:
                    hero['mana'] += 10
                    if hero['mana'] > hero['max_mana']:
                        hero['mana'] = hero['max_mana'] 
                    hero['money'] -= 20
                    print (f'{L118}\nКуплено "Зелье маны". У вас {hero["""mana"""]} ед. маны.')
                else:
                    print ("="*60,"\n","У вас не хватает монет.") 
            elif buy == "2.1" or buy == "2,1" or buy == "большое зелье маны":
                if hero['money'] >= 30:
                    hero['mana'] += 20
                    if hero['mana'] > hero['max_mana']:
                        hero['mana'] = hero['max_mana'] 
                    hero['money'] -= 30
                    print (f'{L118}\nКуплено "Большое зелье маны". У вас {hero["""mana"""]} ед. маны.')
            elif buy == "3" or buy == "далее":
                page = 2 
            
            elif buy == "4" or buy == "продажа" or buy == "продавец":
                if first_dialog == True:
                    first_meeting = input(f"Здравствуй незнакомец, может представишься?\nВаш выбор:\n1. А сам кем будешь?\n2.Я {hero['name']}, а тебя как зовут?\n3. А твоё какое дело? Делай свою работу.")
                    if first_meeting == "1":
                        print (f"Я Старый Гил, скупаю всякое...")
                    elif first_meeting == "2":
                        print (f"Хмм, ты похоже не отсюда родом {hero['inventory']}. Я старый Гил, скупаю вещи всякие.")
                    elif first_meeting == "3":
                        print (f"В непростые времена люди должны доверять друг другу, но ты как я вижу не особо доверяешь другим...")
                print (f"Продавец еще не доделан. Ждите обновлнение 1.1")

                    
            elif buy == "5" or buy == "выход": 
                print (f"Вы вышли из магазина.")
                break
        elif page == 2:
            buy = input(f"{L118}\nМагазин{space*5} (стр 2)\t    Ваш баланс: {hero['money']}\n В наличии:\n 1 -        2 - Далее        3 - Назад\n{L118}\nВаш выбор (1/2): ").lower().strip()
            if buy == "3" or buy == "назад":
                page = 1 
            
    return hero 
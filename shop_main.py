from setting_ui import *
from data import * 
from game_scenes import first_gil
MAX_SLOT = 30 
MAX_PAGE = 3 
def open_shop(hero, world_flag):
    space = " " * 12

    # ---  Магазин --- # 
    
    page = 1
    while True:
        if page == 1:
            print(f"{L118}\nМагазин{space*6}\t\t\t      Ваш баланс: {hero['money']}\nВ наличии: 1 - Зелье здоровья (Восстанавливает 15 хп) стоимость 20 монет.\n1.1 Большое зелье здоровья (Восстанавливает 25 хп) стоимость 30 - монет.\n2. Зелье маны (Восстанавливает 10 ед. маны) стоимость 20 монет.\n2.1 Большое зелье маны (Восстанавливает 20 ед. маны) стоимость 30 монет.     3 - Далее      5 - Выход  0 - Продажа\n{L118} ")
        elif page == 2: 
            print(f"{L118}\nМагазин (стр 2){space*6}\t\t      Ваш баланс: {hero['money']}\nВ наличии: 1 - Палка (+1 урон) стоимость 3 монеты\n1.1 - Копьё каменное (+2 урона) стоимость 6 монет\n2 - Меч каменный (+2 урона) стоимость 7 монет\n2.1 - Железный меч (+4 урона) стоимость 15 монет       3 - Далее       4 - Назад       5 - Выход       0 - Продажа\n{L118}")
        elif page == 3:
            print(f"""{L118}\nМагазин (стр 3){space*6}\t\t      Ваш баланс: {hero['money']}\nВ наличии: 1 - Книга заклинаний "Огненный шар" стоимость 20 монет\n1.1 - Книга заклинаний "Удар молнии" стоимость 16 монет\n2 - Книга заклинаний "Отравление" стоимость 15 монет\n2.1 - Книга заклинаний "Водяной всплеск" стоимость 20 монет      4 - Назад      5 - Выход      0 - Продажа\n{L118}""")
        buy = input("Ваш выбор: ").lower().strip()

        if buy == "3" or buy == "далее": 
            if page < MAX_PAGE: 
                page += 1 
            continue
        elif buy == "4" or buy == "назад":
            if page > 1: 
                page -= 1 
            continue
        elif buy == "5" or buy == "выход": 
            print (f"Вы вышли из магазина.")
            break

        if page == 1:         
            if buy in potion: 
                item = potion[buy]
                if hero['money'] >= item["price"]:
                    hero['money'] -= item['price'] 
                    hero[item['stat']] += item['amount']
                    limit = 'max_' + item['stat']
                    if hero[item['stat']] > hero[limit]: 
                        hero[item['stat']] = hero[limit]
                        print (f"""Вы купили {item['name']}. Восстановленно {item['amount']} {item['stat_name']}""")
                else: 
                    print(f"У вас недостаточно монет.")
                    
        if page == 2:  
            if buy in shop_price_tag_1:
                sword_price_tag = shop_price_tag_1[buy]
                rarity_item = sword_price_tag['rare']
                rarity_id = all_rarity[rarity_item]
                choice_sword = rarity_id[sword_price_tag['name']]
                if len(hero['inventory']) < MAX_SLOT:
                    if hero['money'] >= sword_price_tag['price']:
                        hero['money'] -= sword_price_tag['price']
                        hero['inventory'].append(choice_sword.copy())
                        print(f"""Вы успешно купили {sword_price_tag['name_visual']}""")
                    else: 
                        print(f'У вас недостаточно монет.')
                else:
                    print(f'У вас заполнен инвентарь, освободите место.')

        if page == 3: 
            if buy in shop_price_tag_2:
                spell_id = shop_price_tag_2[buy]['id']
                choice_spell = shop_price_tag_2[buy]
                if spell_id in hero['spells']:
                    print(f"Вы уже изучили это заклинание!")
                else: 
                    if hero['money'] >= choice_spell['price']:
                        hero['money'] -= choice_spell['price'] 
                        hero['spells'].add(spell_id)
                        print(f"""Вы купили {choice_spell['name']}.""")
                    else: 
                        print(f"У вас недостаточно монет.")

        if buy == "продажа" or buy == "продавец" or buy == "0":
            if world_flag["shop_menu"]["first_dialog"] == True:
                hero, world_flag, exit_shop = first_gil(hero, world_flag)
                if exit_shop == True: 
                    return hero, world_flag
            while True:
                if world_flag["shop_menu"]["first_dialog"] == False: 
                    print(f"Привет {hero['name']}, принес что-нибудь на продажу?")
                    print(f"{L104}")
                    print(f"Выберите предмет:{space71}Ваш баланс: {hero['money']}")
                    for i, item in enumerate (hero['inventory']):
                        print (f"{i + 1}. {item['name']}")
                    print(f"{L104}")
                    print(f"0 - Вернуться в магазин.")
                    print(f"{L104}")
                    choice_str = input (f"Ваш выбор: ").lower().strip()
                    print(f"{L104}")
                    if choice_str == "0" or choice_str == "назад":
                        print("Вы вернулись к прилавку.")
                        break

                    elif choice_str.isdigit():
                        choice_item = int(choice_str) - 1
                        if 0 <= choice_item < len(hero['inventory']):
                            index = choice_item
                            selected_item = hero['inventory'][index]
                            confirm_sell = input (f"{selected_item['sale'][1]}\nПродать {selected_item['name']} за {selected_item['sale'][0]}?\nВаш выбор (Да/Нет): ").lower().strip()
                            if confirm_sell == "да" or confirm_sell == "1": 
                                hero['money'] += selected_item['sale'][0]
                                print (f"Вы получили {selected_item['sale'][0]} монет.")
                                hero['inventory'].pop(index)
                                continue
                        else:
                            print(f"Неверный номер предмета.")
                    else:
                        print(f"Введите число.")
    return hero, world_flag
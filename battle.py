MAX_SLOT = 30
from data import * 
from setting_ui import *
import random
import os
def battle(hero):
    while True: #- --- Обновлнение боссов, зацикливание игры --- # 

        # --- Хар-ка боссов --- # 
        name = random.choice(list(bosses.keys()))
        boss_data = bosses[name]
        boss_hp = boss_data[0]
        boss_hit = boss_data[1] 
        money_range = boss_data[2]
        type_boss = boss_data[3]
        boss_money = random.randint(money_range [0], money_range [1])

        print("="*50)
        print(f"Внимание! На вас напал {colorama.Fore.LIGHTRED_EX}{name}{S}")
        print(f"Его здоровье {boss_hp}, а сила удара {boss_hit}.")
        
        while boss_hp > 0 and hero['health'] > 0: # --- Зацикливание одного боя --- # 
            
            # ---  Действие  --- # 
            print(f"Ваше здоровье {hero['health']}/{hero['max_health']}, здоровье босса {boss_hp}.")
            choise = input(f"{L50}\nВаши действия? 1 - Удар, 2 - Бегство, 3 - Выход \n{L50}\nВаш выбор (1/2/3): ").lower().strip()
            if choise == "1" or choise == "удар":
                hit_hero = random.randint(hero['min_damage'], hero['max_damage']) #--- Рассчитываем урон героя ---#
                crit_hero = random.randint(1,100)
                if hero['equipment']['weapon'] is not None:
                    weapon_bonus = hero['equipment']['weapon']['dmg']
                else:
                    weapon_bonus = 0 
                if crit_hero < hero['crit_chance']:
                    crit_hero = hit_hero * 2 
                    total_damage = crit_hero + weapon_bonus
                    boss_hp -= total_damage
                    print (f"{L50}\nВы нанесли критический удар! И снесли врагу {total_damage} хп.")
                    
                else:
                    total_damage = hit_hero + weapon_bonus
                    boss_hp -= total_damage
                    print(f"Вы нанесли боссу {total_damage} урона")
                    
            
                # --- Уклонение, атака босса --- # 
                if boss_hp > 0:
                    if hero['agility'] >= random.randint(1,100):
                        print (f"Вы уклонились от атаки босса!\n{L50}")
                    else:
                        hero['health'] -= boss_hit

                # --- Проверка смерти игрока --- # 
                if hero['health'] <= 0:
                    print(f"{L40}\nВы погибли. Ваши достижения не забудут.\n{L40}")
                    if os.path.exists('save.json'):
                        os.remove('save.json')
                    exit()
                    
                # ---  Проверка смерти босса  --- # 
                if boss_hp <= 0:                        
                    hero['money'] += boss_money
                    hero['stat_point'] += 1 
                
                    boss_drop = random.randint (1,100)
                    # --- Расчёт редкости --- #    
                    if boss_drop <= 10:

                        if len(hero['inventory']) < MAX_SLOT:

                            rare_w = 10 + (hero['luck'] * 0.2)
                            epic_w = 1 + (hero['luck'] * 0.05)
                            lega_w = 0.1 + (hero['luck'] * 0.01)
                            mythic_w = 0.0001 + (hero['luck'] * 0.001)
                            common_w = 100 - (rare_w + epic_w + lega_w + mythic_w)

                            choise_random_rare = [common_items, rare_item, epic_item, legendary_item, mythic_item]
                            chance_drop = [common_w, rare_w, epic_w, lega_w, mythic_w]
                            result_drop = random.choices(choise_random_rare, weights = chance_drop)[0]
                            spisok_predmetov = list(result_drop.keys())
                            item = random.choice(spisok_predmetov)
                            item_for_inventory = result_drop[item].copy()
                            hero['inventory'].append(item_for_inventory)
                            print (f"{L78}\nПоздравляю, босс убит, вы получили {boss_money} монет, а также 1 очко характеристик.\nТакже вы получили {item}\n{L78}")
                        else: 
                            print (f"{L78}\nПоздравляю, босс убит, вы получили {boss_money} монет, а также 1 очко характеристик.\nУ вас заполнен инвентарь, освободите место! (Макс 30)\n{L78}")
                    else:
                        print(f"{L78}\nПоздравляю, босс убит, вы получили {boss_money} монет, а также 1 очко характеристик.\n{L78}")
                
                    # ---  Меню  --- # 
                    menu = input(f"Желаете продолжить? 1 - Да 2 - Нет.\nВаш выбор (1/2): ").lower().strip()
                    if menu == "нет" or menu == "no" or menu == "2":
                        return hero  
            elif choise == "2" or choise == "побег":
                escape = random.randint(1,100)
                if escape >= 30:    
                    print(f"{L50}\nВы успешно сбежали!")
                    break
                else:
                    hero['health'] -= boss_hit
                    print (f"{L50}\nБосс преградил вам дорогу, сбежать не удалось!\nПолучено {boss_hit} урона.\n{L50}")

            elif choise == "3" or choise == "выход":
                print(f"{L50}\nВы успешно вышли!")
                return hero 
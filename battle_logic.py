from setting_ui import * 
import os
from data import *
import random
MAX_SLOT = 30
def check_in_fight(hero, boss_hit, boss_hp, boss_money): 
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
        return True, 0 
    return False, boss_hp
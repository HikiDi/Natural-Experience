MAX_SLOT = 30
from magic import magic_ui
from battle_logic import *
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
        boss_effect_type = "None"
        boss_status_timer = 0
        boss_money = random.randint(money_range [0], money_range [1])

        print("="*58)
        print(f"Внимание! На вас напал {colorama.Fore.LIGHTRED_EX}{name}{S}")
        print(f"Его здоровье {boss_hp}, а сила удара {boss_hit}.")
        
        while boss_hp > 0 and hero['health'] > 0: # --- Зацикливание одного боя --- # 
            
            # ---  Действие  --- # 
            print(f"Ваше здоровье {hero['health']}/{hero['max_health']}, здоровье босса {boss_hp}.")
            choise = input(f"{L58}\nВаши действия? 1 - Удар, 2 - Бегство, 3 - Магия, 4 - Выход \n{L58}\nВаш выбор (1/2/3): ").lower().strip()
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
                    print (f"{L58}\nВы нанесли критический удар! И снесли врагу {total_damage} хп.")
                    
                else:
                    total_damage = hit_hero + weapon_bonus
                    boss_hp -= total_damage
                    print(f"Вы нанесли боссу {total_damage} урона")
                
                is_boss_dead, boss_hp = check_in_fight(hero, boss_hit, boss_hp, boss_money) 
                if is_boss_dead: 

                    # ---  Меню  --- # 
                    menu = input(f"Желаете продолжить? 1 - Да 2 - Нет.\nВаш выбор (1/2): ").lower().strip()
                    if menu == "нет" or menu == "no" or menu == "2":
                        return hero 
                    
            # --- Побег --- #         
            elif choise == "2" or choise == "побег":
                escape = random.randint(1,100)
                if escape >= 30:    
                    print(f"{L58}\nВы успешно сбежали!")
                    break
                else:
                    hero['health'] -= boss_hit
                    print (f"{L58}\nБосс преградил вам дорогу, сбежать не удалось!\nПолучено {boss_hit} урона.\n{L50}")

            # --- Магия --- # 
            elif choise == "3": 
                spells_list = list(hero['spells'])
                print("="*58)
                for i, spell in enumerate (spells_list):
                    print (f"{i + 1}. {spell} ({magic[spell]['mana_cost']} MP)")
                choice_str = input(f"Выберите заклинание для атаки: ")
                if choice_str.isdigit(): 
                    choice = int(choice_str) - 1
                    if 0 <= choice < len(spells_list):
                        spell_choice = spells_list[choice]
                        spell_choice = magic[spell_choice]
                        time_spell = spell_choice.get('duration', 1)
                        if hero['mana'] >= spell_choice['mana_cost']:
                            hero['mana'] -= spell_choice['mana_cost']
                            boss_hp -= spell_choice['damage']
                            print("="*58)
                            print(f"Вы использовали {spell_choice['name']} и нанесли {spell_choice['damage']} урона.")
                            is_boss_dead, boss_hp = check_in_fight(hero, boss_hit, boss_hp, boss_money) 
                            if is_boss_dead:

                             # ---  Меню  --- # 
                                menu = input(f"Желаете продолжить? 1 - Да 2 - Нет.\nВаш выбор (1/2): ").lower().strip()
                                if menu == "нет" or menu == "no" or menu == "2":
                                    return hero  
                        else: 
                            print(f"У вас недостаточно маны.")
                    else: 
                        print(f"Неверное заклинание, повторите попытку.")
                else: 
                    print(f'Выберите число.')

            # --- Выход --- # 
            elif choise == "4" or choise == "выход":
                print(f"{L58}\nВы успешно вышли!")
                return hero 
                        
                        

                    

                    
                
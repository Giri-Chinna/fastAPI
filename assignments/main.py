from enemy import Enemy
from zombie import Zombie
from orge import Orge
from hero import Hero
from weapon import Weapon


def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    print(f"{e1.get_type_of_enemy()} vs {e2.get_type_of_enemy()}")
    while e1.health_points > 0 and e2.health_points > 0:
        print("--------------")
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()} HP: {e1.health_points} vs {e2.get_type_of_enemy()} HP: {e2.health_points}")
        e1.attack()
        e1.health_points -= e2.attack_damage
        e2.attack()
        e2.health_points -= e1.attack_damage
    print("--------------")

    if e1.health_points <= 0 and e2.health_points <= 0:
        print("It's a tie!")
    elif e1.health_points <= 0:
        print(f"{e2.get_type_of_enemy()} wins!")
    else:
        print(f"{e1.get_type_of_enemy()} wins!")

def hero_battle(hero: Hero, enemy: Enemy):

    print(f"Hero vs {enemy.get_type_of_enemy()}")
    while hero.health_points > 0 and enemy.health_points > 0:
        print("--------------")
        enemy.special_attack()
        print(f"Hero HP: {hero.health_points} vs {enemy.get_type_of_enemy()} HP: {enemy.health_points}")
        hero.attack()
        hero.health_points -= enemy.attack_damage
        enemy.attack()
        enemy.health_points -= hero.attack_damage
    print("--------------")

    if hero.health_points <= 0 and enemy.health_points <= 0:
        print("It's a tie!")
    elif hero.health_points <= 0:
        print(f"{enemy.get_type_of_enemy()} wins!")
    else:
        print("Hero wins!")


zombie = Zombie(10, 2)
orge = Orge(30, 3)
hero = Hero(10, 2)
weapon = Weapon("Sword", 10)
hero.weapon = weapon
hero.equip_weapon()

# battle(Zombie(10, 2), Orge(10, 2))
hero_battle(hero, orge)
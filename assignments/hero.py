from typing import Optional
from weapon import Weapon

class Hero:
    def __init__(self, health_points: int, attack_damage: int): 
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon: Optional[Weapon] = None

    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_equipped = True
            print(f"Equipped {self.weapon.weapon_type}")

    def attack(self):
        print(f"Hero attacks for {self.attack_damage} damage")
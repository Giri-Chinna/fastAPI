from enemy import Enemy 
import random

class Orge(Enemy):
    def __init__(self, health_points: int, attack_damage: int):
        super().__init__("Orge", health_points, attack_damage)
    
    def talk(self):
        print("I am a Orge")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.attack_damage += 4
            print("Orge gets stronger and deals 4 more damage") 
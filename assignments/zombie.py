from enemy import Enemy 
import random

class Zombie(Enemy):
    def __init__(self, health_points: int, attack_damage: int):
        super().__init__("Zombie", health_points, attack_damage)
    
    def talk(self):
        print("I am a Zombie")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.health_points += 2
            print("Zombie regenerates 2HP")
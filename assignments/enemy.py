class Enemy:
    def __init__(self, type_of_enemy: str, health_points: int, attack_damage: int):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print("I am an enemy")
    
    def attack(self):
        print(f"{self.get_type_of_enemy()} attacks for {self.attack_damage} damage")

    def special_attack(self):
        print("No special attack")
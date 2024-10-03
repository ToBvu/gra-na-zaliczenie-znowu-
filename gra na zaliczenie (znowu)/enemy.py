import random
from utils import slow_text

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = 5

    def attack(self, player):
        damage = random.randint(int(0.75 * self.strength), int(1.25 * self.strength)) - player.defense
        damage = max(0, damage)  
        player.health -= damage
        slow_text(f"{self.name} atakuje {player.name} i zadaje {damage} obrażeń.", 0.05)

    def is_alive(self):
        return self.health > 0

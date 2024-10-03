import random
from utils import slow_text

class Player:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.inventory = []

    def attack(self, enemy):
        damage = random.randint(int(0.75 * self.strength), int(1.25 * self.strength)) - enemy.defense
        damage = max(0, damage)
        enemy.health -= damage
        slow_text(f"{self.name} atakuje {enemy.name} i zadaje {damage} obrażeń.", 0.05)

    def take_damage(self, damage):
        self.health -= damage
        slow_text(f"{self.name} otrzymuje {damage} obrażeń. Zdrowie: {self.health}", 0.05)

    def is_alive(self):
        return self.health > 0

    def add_to_inventory(self, item):
        self.inventory.append(item)
        slow_text(f"{item.name} został dodany do ekwipunku.", 0.05)

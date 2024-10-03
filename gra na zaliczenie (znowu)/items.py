from utils import slow_text

class Item:
    def __init__(self, name):
        self.name = name

class HealthPotion(Item):
    def __init__(self, name, healing_amount):
        super().__init__(name)
        self.healing_amount = healing_amount

    def use(self, player):
        player.health += self.healing_amount
        slow_text(f"{player.name} użył {self.name} i odzyskał {self.healing_amount} zdrowia.", 0.05)

class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def equip(self, player):
        player.strength += self.damage
        slow_text(f"{player.name} wyposażył się w {self.name}. Siła: {player.strength}", 0.05)

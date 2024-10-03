from utils import slow_text

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_fight(self):
        slow_text(f"Rozpoczyna się walka: {self.player.name} vs {self.enemy.name}", 0.05)
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.attack(self.enemy)
            if self.enemy.is_alive():
                self.enemy.attack(self.player)
        
        if self.player.is_alive():
            slow_text(f"{self.player.name} zwyciężył!", 0.05)
        else:
            slow_text(f"{self.enemy.name} wygrał walkę!", 0.05)

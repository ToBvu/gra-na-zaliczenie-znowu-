from player import Player
from game_map import GameMap
from battle import Battle
from items import HealthPotion, Weapon
from enemy import Enemy
from utils import slow_text

def main():
    game_map = GameMap(5, 5)
    player = Player("Hero", 100, 20, 5)
    enemies = [Enemy("Goblin", 50, 10), Enemy("Orc", 80, 15)]
    items = [HealthPotion("Small Health Potion", 20), Weapon("Sword", 10)]

    slow_text("Witaj w grze RPG!", 0.05)
    slow_text("Eksploruj mapę, walcz z przeciwnikami i zbieraj przedmioty.", 0.05)

    while player.is_alive():
        game_map.display_map()
        action = input("Wybierz akcję (move, fight, quit): ").lower()
        
        if action == "move" or action == "m":
            direction = input("Wybierz kierunek (north, south, east, west), [w,s,a,d]: ").lower()
            game_map.move_player(direction)
        
        elif action == "fight" or action == "f":
            if enemies:
                enemy = enemies.pop(0)
                battle = Battle(player, enemy)
                battle.start_fight()
            else:
                slow_text("Brak przeciwników do walki!", 0.05)
        
        elif action == "quit" or action == "q":
            slow_text("Dziękujemy za grę!", 0.05)
            break
        
        else:
            slow_text("Nieznana akcja. Spróbuj ponownie.", 0.05)
    
    if not player.is_alive():
        slow_text("Przegrałeś! Koniec gry.", 0.05)
    else:
        slow_text("Koniec gry. Wygrałeś!", 0.05)

if __name__ == "__main__":
    main()

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player_position = [0, 0]

    def display_map(self):
        for y in range(self.height):
            for x in range(self.width):
                if [x, y] == self.player_position:
                    print("P", end='')  
                else:
                    print(".", end='')  
            print('')  

    def move_player(self, direction):
        if direction == "north" and self.player_position[1] > 0 or direction == "w" and self.player_position[1] > 0:
            self.player_position[1] -= 1
        elif direction == "south" and self.player_position[1] < self.height - 1 or direction == "s" and self.player_position[1] < self.height - 1:
            self.player_position[1] += 1
        elif direction == "east" and self.player_position[0] < self.width - 1 or direction == "d" and self.player_position[0] < self.width - 1:
            self.player_position[0] += 1
        elif direction == "west" and self.player_position[0] > 0 or direction == "a" and self.player_position[0] > 0:
            self.player_position[0] -= 1
        else:
            print("Nie możesz iść w tym kierunku.")

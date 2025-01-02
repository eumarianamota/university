# Mariana da Mota Pinho
# Sofia Khrisla Santos Rocha

import random

class DominoTile:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def __str__(self):
        return f"({self.number1}, {self.number2})"   
    
    def flip(self):
        self.number1, self.number2 = self.number2, self.number1
        return self.number1, self.number2

    def is_double(self):
        return print(self.number1 == self.number2)

class DominoSet:
    def __init__(self):
        self.__tiles = []  

    def generate_tiles(self):
        for i in range(7):
            for j in range(i, 7):
                tile = DominoTile(i, j)
                self.__tiles.append(tile)

    def shuffle_tiles(self):
        random.shuffle(self.__tiles)

    def show_tiles(self):
        print("As peças de dominó disponíveis são:")
        for tile in self.__tiles:
            print(tile)

    def pick_tiles(self, n):
        print("As peças removidas são:")
        removed_tiles = random.sample(self.__tiles, k=n)
        for tile in removed_tiles:
            self.__tiles.remove(tile)
            print(tile)



dominos  = DominoSet()
dominos.generate_tiles()
dominos.shuffle_tiles()
dominos.pick_tiles(5)
dominos.show_tiles()

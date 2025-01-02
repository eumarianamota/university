# Mariana da Mota Pinho
# Sofia Khrisla Santos Rocha
import random 

class DominoTile:
  def __init__(self, number1, number2):
    self.number1 = number1
    self.number2 = number2

  def __str__(self):
    return f'({self.number1}, {self.number2})'

  def flip(self): 
    self.new_1 = self.number2
    self.new_2 = self.number1  

  def is_double(self):
    return self.number1 == self.number2


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

  def pick_tiles(self, n):
    removed_tiles = random.choices(self.__tiles, k = n)

    for x in removed_tiles:
      self.__tiles.remove(x)

    for tile in removed_tiles:
        print(tile, end= " ")


  def show_tiles(self):
    for tile in self.__tiles:
      print(tile, end= " ")


domino = DominoSet()
domino.generate_tiles()
domino.shuffle_tiles()
domino.pick_tiles(5)
domino.show_tiles()
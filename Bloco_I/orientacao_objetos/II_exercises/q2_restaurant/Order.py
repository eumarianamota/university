from Item import Item

class ItemNotFoundError(Exception):
  pass

class ItemAlreadyExistsError(Exception):
  pass

class Order:
  def __init__(self):
    self.items = []

  def add_item(self, item):
    if item in self.items:
      raise ItemAlreadyExistsError(f'O {item} já está na lista')
    self.items.append(item)
  
  def remove_item(self, item):
    if item in self.items:
      index = self.items.index(item)
      self.items.pop(index)
    else:
      raise ItemNotFoundError(f'O {item} não está na lista')

  def show_order(self):
    self.total_price = 0
    print("Order items:")
    for item in self.items:
      print(f"- {item.name}: ${item.price}")
      self.total_price += item.price
    print(f"Price: ${self.total_price}")

  def __str__(self):
    return f'{self.items}'
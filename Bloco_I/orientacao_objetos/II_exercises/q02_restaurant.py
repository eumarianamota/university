# Simule um sistema de pedidos em um restaurante. Implemente:
# 1. Classe Item :
  # Atributos: name, price .
# 2. Classe Order :
  # Atributos: items (lista de objetos Item).
# Métodos:
  # add_item(item) : Adiciona um item ao pedido. Caso o item já esteja no pedido, lance uma exceção ItemAlreadyExistsError .
  # remove_item(item_name) : Remove o item pelo nome. Caso o item não exista no pedido, lance uma exceção ItemNotFoundError .
  # show_order() : Exibe todos os itens no pedido e o total parcial.
# 3. Classe Bill :
  # Atributos: order e service_fee (10% do total do pedido).
# Métodos:
  # calculate_total() : Calcula o total com a taxa de serviço.
  # show_bill() : Exibe o total final, incluindo o detalhamento dos itens e a taxa.

class Item:
  def __init__(self, name, price):
    self.name = name
    self.price =  price


class Order:
  def __init__(self):
    self.items = []
    self.items.extend(Item)
    print(self.itens)

  def add_item(self, name, price):
    item = name, price
    self.items.append(item)
    print(self.items)
  

pizza = 'pizza', 30
batata = 'batata frita', 15
coca = 'coca cola', 5

pedidos = pizza



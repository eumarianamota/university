# Simule um sistema de pedidos em um restaurante. Implemente:

# 1. Classe Item :
  # Atributos: name, price.

# 2. Classe Order :
  # Atributos: items (lista de objetos Item).
# Métodos:
  # add_item(item) : Adiciona um item ao pedido. Caso o item já esteja no pedido, lance uma exceção ItemAlreadyExistsError .
  # remove_item(item_name) : Remove o item pelo nome. Caso o item não exista no pedido, lance uma exceção ItemNotFoundError .
  # show_order() : Exibe todos os itens no pedido e o total parcial.

# 3. Classe Bill :
  # Atributos: order e service_fee (10% do total do pedido).
#Métodos:
  # calculate_total() : Calcula o total com a taxa de serviço.
  # show_bill() : Exibe o total final, incluindo o detalhamento dos itens e a taxa.

class Item:
  def __init__(self, name, price):
    self.name = name
    self.price =  price
  
  def __str__(self):
    return f'{self.name} - {self.price}'
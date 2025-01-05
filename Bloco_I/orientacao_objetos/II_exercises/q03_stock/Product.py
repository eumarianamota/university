#Classe Product :
# Atributos: name , quantity , expiry_date (como uma string no formato dd/mm/yyyy ).
# Métodos:
# add_stock(amount) : Incrementa o estoque. Caso o valor seja negativo, lance uma exceção InvalidStockValueError .
# remove_stock(amount) : Decrementa o estoque, desde que não fique negativo. Caso a quantidade não seja suficiente, lance uma exceção InsufficientStockError.
# check_expiry(current_date) : Verifica se o produto está vencido comparando a validade com a data atual fornecida como argumento. Caso a data esteja mal formatada, lance uma exceção InvalidDateFormatError.
class InvalidStockValueError(Exception):
  pass

class InsufficientStockError(Exception):
  pass

class Product:
  def __init__(self, name, quantity, expiry):
    self.name = name
    self.quantity = quantity
    self.expiry_date = expiry.split('/')

  
  def add_stock(self, quantity):
    if quantity < 0:
      raise InvalidStockValueError('A quantidade inserida é invalida')
    self.quantity += quantity
  
  def remove_stock(self, quantity):
    if quantity < 0:
      raise InsufficientStockError('A quantidade inserida é inválida')
    if quantity > self.quantity:
      raise InsufficientStockError('O estoque é menor que a quantidade que você deseja decrementar')
    self.quantity -= quantity
  
  def check_expiry(self, date):
    date = date.split('/')
    if int(date[-1]) > int(self.expiry_date[-1]):
      print("VALIDADE: está vencido")
    elif int(date[-2]) > int(self.expiry_date[-2]):
      print("VALIDADE: está vencido")
    elif int(date[0]) > int(self.expiry_date[0]):
      print("VALIDADE: está vencido")
    else: 
          print('VALIDADE: não está vencido')

  def show_stock(self):
    print('STOCK:')
    print(f'{self.name} | {self.quantity} | {self.expiry_date[0]}/{self.expiry_date[1]}/{self.expiry_date[-1]}')
    print('')


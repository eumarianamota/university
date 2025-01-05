class Bill:
  def __init__(self, order):
    self.order = order
    self.service_fee = 0.1
  
  def __str__(self):
    return f'{self.order}'
  
  def calculate_total(self):
    total_price = 0

    for i in self.order.items:
      total_price += i.price
    
    self.tax = total_price * self.service_fee
    self.total = total_price + self.tax

  def show_bill(self):
    print(f'Items:')
    for i in self.order.items:
      print(i)
    print(f'Servic fee: R${self.tax}')
    print(f'Total price:R${self.total}')
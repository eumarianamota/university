# Crie uma classe BankAccount com:
# Atributos:
  # holder (nome do titular, fornecido no construtor).
  # balance (valor inicial, padrão 0).
# Métodos:
  # deposit(amount) - adiciona ao saldo.
  # withdraw(amount) - reduz o saldo (somente se houver saldo suficiente).
  # print_balance() - exibe o saldo atual.
# Defina o formato da string de representação do objeto para: BankAccount(Fulano de Tal; R$2.197,53) , onde Fulano de Tal é o nome do cliente e R$2.197,53 o saldo.

class bankAccount:
  def __init__(self, holder, balance = 0):
    self.holder = holder
    self.balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
  
  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
  
  def __str__(self):
    return f'BankAccount({self.holder}; {self.balance})'
  
  def print_balance(self):
    print(f'{self.balance}')
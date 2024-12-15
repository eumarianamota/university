#Crie um projeto do VS Code para conter os arquivos da lista de exercícios
#Habilite a extensão Python do VS Code para suporte à linguagem Python 3

# Crie uma classe chamada Lamp com:
# Atributos:
  # state (indica se está ligada ou desligada, inicialize como "off").
# Métodos:
  # turn_on() - altera o estado para "on".
  # turn_off() - altera o estado para "off".
  # print_state() - imprime o estado atual.

class lamp:
  def __init__(self, initial_state = False):
    if initial_state: #se você não coloca false ou true, significa que é true 
      self.state = 'on'
    else:
      self.state = 'off'
  
  def turn_on(self):
    self.state = 'on'
  
  def turn_off(self):
    self.state = 'off'

  def print_state(self):
    print(f'Lamp is {self.state}')
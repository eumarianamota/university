# Adicionando atributos personalizados
# Amplie o exercício anterior. Adicione:
  # Um atributo chamado color (ex.: "white", "yellow").
  # Um atributo chamado power (potência da lâmpada em Watts).
  # Um método para modificar a cor: set_color(new_color) .
  # Um método para modificar a potência: set_power(new_color) .
  # Utilize o método mágico __str__() para definir um string de representação para o objeto. A string deverá ser formatada como no exemplo:
# Lamp(30W,white,on) , onde 30W é a potẽncia, white a cor e on o estado.

class lamp:
  def __init__(self, color, power, initial_state = False):
    if initial_state:
      self.state = 'on'
    else:
      self.state = 'off'
    
    self.color = color
    self.power = power
  
  def __str__(self):
    return f'Lamp({self.power}, {self.color}, {self.state})'
  
  def turn_on(self):
    self.state = 'on'
  
  def turn_off(self):
    self.state = 'off'

  def set_color(self, color):
    self.new_color = color

  def print_state(self):
    print(f'lamp is {self.state}')


lampada = lamp('pink', 30, True)
print(lampada)
lampada.print_state()
# Crie uma classe Temperature com:
# Um atributo privado _celsius .
# Métodos:
# set_temperature(value) - permite alterar o valor de _celsius (apenas se for maior ou igual a -273.15).
# get_temperature() - retorna o valor de _celsius .

class Temperature:
  def __init__(self, celsius):
    self._celsius = None
  
  def set_temperature(self, temperature):
    if temperature >= -273.15:
      self._celsius = temperature
  
  def get_temperature(self):
    return self._celsius
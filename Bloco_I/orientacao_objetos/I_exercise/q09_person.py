# Crie uma classe Person com:
# Atributos:
  # Privados: _name , _age .
# Métodos:
  # get_name() e get_age() - retornam os valores de _name e _age .
  # set_name(name) e set_age(age) - permitem alterar _name e _age (valide a idade para que seja um número positivo).

class Person:
  def __init__(self, name, age):
    self.__name = self.set_name(name)
    self.__age = self.set_age(age)
  
  def get_name(self):
    return self.__name

  def get_age(self):
    return self.__age

  def set_name(self, new_name):
    self.__name = new_name
    return self.__name
  
  def set_age(self, age):
    if age < 0:
      raise ValueError('A idade tem que ser maior que 0')
    return age

nome = Person('mariana', 18)
print(nome.get_name())
print(nome.get_age())
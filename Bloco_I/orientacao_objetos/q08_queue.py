# Crie uma classe Queue para simular uma fila de atendimento com:
# Atributos:
# Uma lista privada _people .
# Métodos:
# add_person(name) - adiciona uma pessoa no final da fila.
# remove_person() - remove a primeira pessoa da fila.
# show_queue() - exibe a fila atual.

class Queue:
  def __init__(self, people):
    self._people = []
  
  def add_person(self, name):
    self._people.append(name)
  
  def remove_person(self):
    self._people.remove(0)
  
  def show_queue(self, _people):
    for peoplee in _people:
      print(peoplee)
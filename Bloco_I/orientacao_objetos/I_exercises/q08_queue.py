# Crie uma classe Queue para simular uma fila de atendimento com:
# Atributos:
# Uma lista privada _people .
# Métodos:
# add_person(name) - adiciona uma pessoa no final da fila.
# remove_person() - remove a primeira pessoa da fila.
# show_queue() - exibe a fila atual.

class Queue:
  def __init__(self):
    self._people = []
  
  def add_person(self, name):
    self._people.append(name)
    return self._people
  
  def remove_person(self):
    self._people.pop(0)
    return self._people
  
  def show_queue(self):
    for person in self._people:
      print(person)

lista1 = Queue()

print(lista1.add_person('Mariana'))
print(lista1.add_person('Julia'))
print(lista1.add_person('Rhuan'))
print(lista1.add_person('Laisa'))
print(lista1.add_person('Clarissa'))

print(lista1.show_queue())
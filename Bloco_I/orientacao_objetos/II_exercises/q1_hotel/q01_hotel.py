# Implemente um sistema para gerenciar reservas em um hotel. Crie uma classe Hotel com:
# Atributos:
  # rooms : Um dicionário onde as chaves são números de quartos (ex.: 101, 102, 103) e os valores representam o status do quarto ( "occupied" ou "available" ).
# Métodos:
  # check_in(room_number) : Marca um quarto como "occupied" , verificando se ele está "available" . Caso o quarto esteja ocupado, lance uma exceção personalizada RoomOccupiedError.
  # check_out(room_number) : Marca um quarto como "available" , verificando se ele está "occupied" . Caso o quarto já esteja disponível, lance uma exceção RoomAlreadyAvailableError .
  # show_status() : Mostra o status de todos os quartos.

class RoomOccupiedError(Exception):
  pass

class RoomAlreadyAvailableError(Exception):
  pass

class Hotel:
  def __init__(self, *room_numbers):
    self.rooms = {room_number: "Available" for room_number in room_numbers} #for x in y é um loop que itera sobre todos os elementos de y.
  
  def check_in(self, room_number):
    if self.rooms.get(room_number) == "Available":
      self.rooms[room_number] = "Ocuppied"
      return self.rooms[room_number]
    raise RoomOccupiedError(f'O quarto {room_number} está ocupado.')
  
  def check_out(self, room_number):
    if self.rooms.get(room_number) == 'Ocuupied':
      self.rooms[room_number] = "Available"
      return self.rooms[room_number]
    raise RoomAlreadyAvailableError(f'O quarto {room_number} já está disponível.')

  def show_status(self):
    for i in self.rooms:
      print(self.rooms[i])


palace = Hotel(101, 102, 103, 104, 105, 106, 107, 108, 109, 110)
palace.check_in(107)
palace.check_in(105)
palace.check_in(103)
palace.show_status()
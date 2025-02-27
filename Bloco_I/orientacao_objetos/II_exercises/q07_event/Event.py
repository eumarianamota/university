# 1. Classe Event :
# Atributos: name , date , time , location .
# 2. Classe Agenda :
# Atributos: Lista de eventos.
# Métodos:
# add_event(event) : Adiciona um evento à lista. Caso já exista um evento com o mesmo nome e horário, lance uma exceção EventConflictError .
# remove_event(event_name) : Remove um evento pelo nome. Caso o evento não exista, lance uma exceção EventNotFoundError .
# list_events(date) : Exibe eventos agendados para uma data específica.

class Event:
  event = []

  def __init__(self, name, date, time, location):
    self.name = name 
    self.date = date 
    self.time = time
    self.location = location
    Event.event.append([self.name, self.date, self.time, self.location])
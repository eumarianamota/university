from Event import Event 

class EventConflicError(Exception):
    pass

class Agenda:
    def __init__(self):
        self.events = Event.event
    
    def add_event(self, name, date, time, location):
        for i in self.events:
            if i[0] == name and i[1] == time: 
                raise EventConflicError('Já existe um evento com esse nome e data')
            else:
                self.events.append([name, date, time, location])
        print(self.events)

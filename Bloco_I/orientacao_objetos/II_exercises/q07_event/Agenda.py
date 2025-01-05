from Event import Event 

class EventConflicError(Exception):
    pass

class Agenda:
    def __init__(self):
        self.events = Event.event
    
    def add_event(self, name, date, time, location):
        for i in self.events:
            if (i[0] == name) and (i[2] == time): 
                raise EventConflicError('Já existe um evento com esse nome e data')
            else:
                self.events.append([name, date, time, location])
    
    def remove_event(self, name):
        for i in self.events:
            if i[0] == name:
                self.events.remove(i)
    
    def list_events(self, date):
        for i in self.events:
            if i[1] == date:
                print(f'{i[0]}, {i[1]}, {i[2]}, {i[3]}')

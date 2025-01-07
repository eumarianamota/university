from Event import Event 

class EventConflicError(Exception):
    pass

class EventNotFoundError(Exception):
    pass

class Agenda:
    def __init__(self):
        self.events = Event.event

    def add_event(self, name, date, time, location):
        if [name, date, time, location] in self.events:
            raise EventConflicError('Já existe um evento com esse nome e horário')
        else:
            self.events.append([name, date, time, location])
    
    def list_events(self, date):
        for i in self.events:
            if i[1] == date:
                print(f'{i[0]}, {i[1]}, {i[2]}, {i[3]}')

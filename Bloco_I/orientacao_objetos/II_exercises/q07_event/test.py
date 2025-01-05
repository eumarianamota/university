from Event import Event 
from Agenda import Agenda

casamento = Event('Nath e Lusca', '25/06/2022', '16:00', 'Paris, França')
aniversario = Event('Mariana', '02/04/2025', '20:00', 'Minha casa')
formatura = Event('Mariana Forms', '15/01/2027', '22:00', 'Faustino')
confra = Event('Mariana', '15/01/2027', '22:00', 'Faustino')
niver = Event('Lucy', '15/01/2027', '22:00', 'Faustino')

agenda = Agenda()
agenda.list_events('15/01/2027')


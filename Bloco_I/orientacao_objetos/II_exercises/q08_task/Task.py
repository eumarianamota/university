# Classe Task :
# Atributos: name , description , priority ( low , medium , high ).
# 2. Classe TaskManager :
# Atributos: Uma lista de tarefas.
# Métodos:
# add_task(task) : Adiciona uma nova tarefa. Caso já exista uma tarefa com o mesmo nome, lance uma exceção
# TaskAlreadyExistsError .
# remove_task(task_name) : Remove uma tarefa pelo nome. Caso a tarefa não exista, lance uma exceção TaskNotFoundError .
# list_tasks(priority=None) : Lista todas as tarefas ou filtra por prioridade.
class PriorityClassError(Exception):
  pass

class Task:
    def __init__(self, name, description, priority):
        if priority not in ['Low', 'Medium', 'High']:
            raise PriorityClassError('The priority must be low, medium or high')
        
        self.priority = priority
        self.name = name 
        self.description = description

    def __str__(self):
        return f'{self.name} - {self.description} - {self.priority}'

    def __repr__(self):
        return self.__str__()
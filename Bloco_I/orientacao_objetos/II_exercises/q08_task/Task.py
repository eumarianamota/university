# Classe Task :
# Atributos: name , description , priority ( low , medium , high ).
# 2. Classe TaskManager :
# Atributos: Uma lista de tarefas.
# Métodos:
# add_task(task) : Adiciona uma nova tarefa. Caso já exista uma tarefa com o mesmo nome, lance uma exceção
# TaskAlreadyExistsError .
# remove_task(task_name) : Remove uma tarefa pelo nome. Caso a tarefa não exista, lance uma exceção TaskNotFoundError .
# list_tasks(priority=None) : Lista todas as tarefas ou filtra por prioridade.
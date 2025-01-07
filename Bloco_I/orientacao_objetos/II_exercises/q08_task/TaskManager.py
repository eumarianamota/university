from Task import Task

class TaskAlreadyExistsError(Exception):
		pass 

class TaskNotFoundError(Exception):
    pass

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        for task in self.tasks:
            if Task.name == task:
                raise TaskAlreadyExistsError('ja existe')
            print(task)



    def remove_task(self, name):
        for task in self.tasks:
            if Task.name == name:
                self.tasks.remove(task)
                return 
        raise TaskNotFoundError("Task doesn't exist")



clean = Task('Clean the house', 'Clean the bedroom', 'Medium')
dishes = Task('Wash the dishes', 'Wash all the dishes from dinner', 'High')

tasks = TaskManager()
tasks.add_task(clean)
tasks.add_task(dishes)
tasks.add_task(dishes)



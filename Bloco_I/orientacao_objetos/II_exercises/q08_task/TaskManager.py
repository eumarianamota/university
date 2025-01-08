from Task import Task

class TaskAlreadyExistsError(Exception):
		pass 

class TaskNotFoundError(Exception):
    pass

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        for k in self.tasks:
            if task == k:
                raise TaskAlreadyExistsError('This task already exist')
        self.tasks.append(task)
    
    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                return self.tasks.remove(task)
        raise TaskNotFoundError("Task doesn't exist")
    
    def list_tasks(self, priority=None):
        if priority == None:
            print('ALL THE TASKS')
            for task in self.tasks:
                print(task)
                print('_'*50)
        elif priority == 'Low':
            print('TASKS WITH LOW PRIORITY')
            print('_'*50)
            for task in self.tasks:
                if task.priority == 'Low':
                    print(task)
                    print('_'*50)
        elif priority == 'Medium':
            print('TASKS WITH MEDIUM PRIORITY')
            print('_'*50)
            for task in self.tasks:
                if task.priority == 'Medium':
                    print(task)
                    print('_'*50)
        elif priority == 'High':
            print('TASKS WITH HIGH PRIORITY')
            print('_'*50)
            for task in self.tasks:
                if task.priority == 'High':
                    print(task)
                    print('_'*50)



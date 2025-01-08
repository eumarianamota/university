from Task import Task
from TaskManager import TaskManager

def main():
    clean = Task('Clean', 'Clean the bedroom', 'Medium')
    cleann = Task('Clean', 'Clean the bedroom', 'Low')
    cleean = Task('Clean', 'Clean the bedroom', 'Medium')
    cleaan = Task('Clean', 'Clean the bedroom', 'Low')
    dishes = Task('Wash the dishes', 'Wash all the dishes from dinner', 'High')

    tasks = TaskManager()
    tasks.add_task(clean)
    tasks.add_task(cleann)
    tasks.add_task(cleaan)
    tasks.add_task(cleean)
    tasks.add_task(dishes)

    tasks.remove_task('Clean')
    tasks.list_tasks('Low')
    tasks.list_tasks('High')
    tasks.list_tasks('Medium')
    tasks.list_tasks()

if __name__ == '__main__':
    main()
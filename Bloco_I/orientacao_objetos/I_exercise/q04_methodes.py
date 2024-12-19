# Crie uma classe Employee com:
# Atributos:
  # name e salary .
  # Um atributo de classe total_employees para contar quantos objetos da classe foram criados.
# Métodos:
  # __init__() - inicializa o objeto e incrementa total_employees .
  # show_total_employees() - exibe o número total de funcionários.
  # Defina string de representação do objeto para ser o nome do funcionário.

class Employee:
  total_employees = 0 # um atributo de classe é definido fora do construtor.

  def __init__(self, name, salary):
    Employee.total_employees += 1

    self.name = name 
    self.salary = salary

  def __str__(self, name):
    return f'{name}'

  def show_total_employees(total_employees):    
    print(f'{Employee.total_employees}')
class Employee:
  def __init__(self, name, position, salary, numberOfChildren):
    self.name = name
    self.position = position
    self.salary = salary
    self.numberOfChildren = numberOfChildren

  def get_net_salary(self):
    return self.salary - (self.salary * 0.15 - self.numberOfChildren * 1500)

frantisek = Employee("František Novák", "účetní", 10000, 2)
print(frantisek.get_net_salary())
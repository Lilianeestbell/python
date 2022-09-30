class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, added_salary=''):
        if added_salary:
            self.salary += added_salary
        else:
            self.salary += 5000

one_employee = Employee('lily', 'brown', 2000)
one_employee.give_raise(7000)
print(one_employee.salary)
# Define a class Employee with insantce object variables empid, name, salary,. Write __init__()
# method in the class to initialize instance object variables. Also define insatnce methods to input fields and display field values

class Employee:
    
    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary
        
    def display(self):
        print(f'Empid: {self.empid}')
        print(f'Name: {self.name}')
        print(f'Salary: {self.salary}')
        
employee1 = Employee(1, 'Tyrion', 175000 )

employee1.display()
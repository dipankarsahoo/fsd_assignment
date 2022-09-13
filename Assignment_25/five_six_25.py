# Write a python script to create a Calculator class with 2 methods for adding and
# subtracting 2 values

class Calculator:
    
    def __init__(self,  a, b):
        self.a , self.b = a, b
        
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
calculation1 = Calculator(5, 3)

print(f'addition result = {calculation1.add()}')
print(f'subtraction result = {calculation1.subtract()}')

# Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
# and division of 2 values and inherit it from the Calculator class.

class Calculator2(Calculator):
    
    def __init__(self, a, b):
        super().__init__(a, b)
        
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        return self.a / self.b
    
calculation2 = Calculator2(5, 3)

print(f'addition result = {calculation2.add()}')
print(f'subtraction result = {calculation2.subtract()}')
print(f'multiplication result = {calculation2.multiply()}')
print(f'division result = {calculation2.divide()}')
        
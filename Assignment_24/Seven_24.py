# Write a python program to create a Laptop class with 4 attributes(brand, ram, cpu, hdd) and 2 methods (showConfig() to print the values , __init__ to initialize the values)

class Laptop:
    
    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd
        
    def showConfig(self):
        print(f'The laptop is of {self.brand} brand')
        print(f'The laptop has {self.ram} GB ram')
        print(f'The laptop has {self.cpu} CPU')
        print(f'The laptop has {self.hdd} TB HDD')
        
laptop1 = Laptop('HP', 32, 'i9', 2)

laptop1.showConfig()
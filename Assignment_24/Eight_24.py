# WRT 7 create 3 laptop objects and add them to the list in the sorted order based on ram size.


class Laptop:    
    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd
        # laptops = laptops.append(self)
        
    def showConfig(self):
        print(f'The laptop is of {self.brand} brand')
        print(f'The laptop has {self.ram} GB ram')
        print(f'The laptop has {self.cpu} CPU')
        print(f'The laptop has {self.hdd} TB HDD')
        
    # def sorted_laptops(self):
    #     self.laptops.sort(key=lambda x: x.ram, reverse=True)
    #     return self.laptops
        

laptop1 = Laptop('HP', 64, 'i9', 2)
laptop2 = Laptop('Asus', 16, 'i5', 1.5)
laptop3 = Laptop('Lenovo', 8, 'i3', 1)

# Sorting outside class
laptop_list = [laptop1, laptop2, laptop3]
laptop_list.sort(key=lambda x: x.ram, reverse=True)

for laptop in laptop_list:
    print(f'The laptop {laptop.brand} has {laptop.ram}')
          

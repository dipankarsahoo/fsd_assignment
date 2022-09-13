# Write a python script to create an application like Truecaller where names and
# numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
# number and 2nd to add a new entry).

class Truecaller():
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.phonebook = {name: number}
        
    def fetchName(self, number):
        names = list(self.phonebook.keys())
        numbers = list(self.phonebook.values())
        position = numbers.index(number)
        return names[position]
    
    def addNumber(self, name, number):
        if name in self.phonebook.keys():
            self.phonebook[name] = [self.phonebook[name], number]
        else:
            self.phonebook[name] =  number
            

caller = Truecaller('Jhon Smith', 958745875)
print(f'Caller name : {caller.fetchName(958745875)}')

caller.addNumber('Kate Moss', 5784578548)
print(f'Caller name : {caller.fetchName(5784578548)}')

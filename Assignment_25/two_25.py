# Write a python script to update the above Profile class with encapsulation.

class Profile():
    
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
    def display(self):
        print(f'Profile name : {self.name}')
        print(f'Profile email : {self.email}')
        print(f'Profile age : {self.age}')
        
profile1 = Profile('Daemon', 'daemon.ta@gmail.com', 25)
    
profile1.display()
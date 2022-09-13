# Write a python script to create a Profile class with 3 attributes (name, email, age).

class Profile():
    
    name = 'Daemon' 
    age = 20
    email = 'daemon.ta@gmail.com'
        
    def display(self):
        print(f'Profile name : {self.name}')
        print(f'Profile email : {self.email}')
        print(f'Profile age : {self.age}')
        
profile1 = Profile()
    
profile1.display()
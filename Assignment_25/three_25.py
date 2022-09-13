# Write a python script to update 2nd Question, change email and age to __email and
# __age.

class Profile():
    
    def __init__(self, name, email, age):
        self.name = name
        self.__email = email
        self.__age = age
        
    def display(self):
        print(f'Profile name : {self.name}')
        print(f'Profile email : {self.__email}')
        print(f'Profile age : {self.__age}')
        
profile1 = Profile('Daemon', 'daemon.ta@gmail.com', 27)
    
profile1.display()
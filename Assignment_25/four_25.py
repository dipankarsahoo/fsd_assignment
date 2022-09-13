# Write a python script to update 2nd Question, add a class variable (platform) and
# create a classmethod to access it.

class Profile():
    platform = 'Instagram'
    
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
    def display(self):
        print(f'Profile name : {self.name}')
        print(f'Profile email : {self.email}')
        print(f'Profile age : {self.age}')

    @classmethod
    def printPlatform(cls):
        print(f'Platform : {cls.platform}') 
        
profile1 = Profile('Daemon', 'daemon.ta@gmail.com', 25)
    
profile1.display()

Profile.printPlatform()
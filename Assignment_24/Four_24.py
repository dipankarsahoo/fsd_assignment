# Write a python program to init default values for user object using __init__ method

class user:
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def greet_user(self):
        print(f'Hello ! {self.name}')

User1 = user('John Smith', 20, 'john.smith@gmail.com')
User1.greet_user()

User2 = user('Samwell Tarly', 22, 'samwell.tarly@gmail.com')
User2.greet_user()

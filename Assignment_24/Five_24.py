# Write a python program to delete age attribute of the user

class user:
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def greet_user(self):
        print(f'Hello ! {self.name}')
        print(f'Your email is {self.email}')
        # print(f'Your age is {self.age}')   # AttributeError: 'user' object has no attribute 'age'

User1 = user('John Smith', 20, 'john.smith@gmail.com')
del User1.age
User1.greet_user()

User2 = user('Samwell Tarly', 22, 'samwell.tarly@gmail.com')
del User2.age
User2.greet_user()

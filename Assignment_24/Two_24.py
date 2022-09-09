# Write a python program to create a user class with a method to greet the user
class user:
    
    def greet_user(self):
        print(f'Hello ! {self.name}')

User = user()

User.name = 'John Smith'
User.age = 20
User.email = 'john.smith@gmail.com'

User.greet_user()
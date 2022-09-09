# Write a python program to create 2 objects of user class and assign different values

class user:
    
    def greet_user(self):
        print(f'Hello ! {self.name}')

User1 = user()

User1.name = 'John Smith'
User1.age = 20
User1.email = 'john.smith@gmail.com'

User2 = user()

User2.name = 'Samwell Tarly'
User2.age = 22
User2.email = 'samwell.tarly@gmail.com'

User1.greet_user()
User2.greet_user()

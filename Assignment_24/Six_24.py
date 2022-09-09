# Write a python program to create 3 user and find youngest of all
class user:    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def greet_user(self):
        print(f'Hello ! {self.name}')
        
    def youngest(user1, user2, user3):
        if user1.age < user2.age and user1.age < user3.age:
            return user1
        elif user1.age > user2.age and user2.age < user3.age:
            return user2
        else:
            return user3

User1 = user('John Smith', 30, 'john.smith@gmail.com')
User1.greet_user()

User2 = user('Samwell Tarly', 32, 'samwell.tarly@gmail.com')
User2.greet_user()

User3 = user('Edward Stark', 25, 'edward.stark@gmail.com')
User3.greet_user()

# OOPS way to find youngest
young = user.youngest(User1, User2, User3)
print(f'Youngest is {young.name}')

# Using inplace list sorting
# User_list = [User1, User2, User3]
# User_list.sort(key=lambda x: x.age, reverse=False)
# print(f'Youngest is {User_list[0].name}')
# Write a python script to create a user account class with 2 instance variables (userid
# and balance). Create 3 user objects and add all the users using operator
# overloading.

class UserAccount():
    def __init__(self, userid, balance):
        self.userid = userid
        self.balance = balance
        
    def __add__(self, other ):
        return UserAccount('Users Total', (self.balance + other.balance))
    
user1 = UserAccount('user1', 2000)
user2 = UserAccount('user2', 1205.70)
user3 = UserAccount('user3', 4000)

Total_balance = user1 + user2 + user3

print(Total_balance.balance)
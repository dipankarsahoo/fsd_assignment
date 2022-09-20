# Write a python script to create a to print the above user account object using operator
# overloading (hint __str__ method)

class UserAccount():
    def __init__(self, userid, balance):
        self.userid = userid
        self.balance = balance
        
    def __add__(self, other ):
        return UserAccount('Users Total', (self.balance + other.balance))
    
    def __str__(self):
        return self.userid
    
user1 = UserAccount('user1', 2000)
user2 = UserAccount('user2', 1205.70)
user3 = UserAccount('user3', 4000)

Total_balance = user1 + user2 + user3

print(Total_balance.balance)
print(Total_balance)
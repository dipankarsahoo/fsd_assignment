# Write a python script to create a Phone class with 2 methods to print the features
# (calling and sms).

class Phone:
    
    def __init__(self, calling, sms):
        self.calling = calling
        self.sms = sms
        
    def callingValue(self):
        return self.calling
    
    def smsValue(self):
        return self.sms
    
    
iphone = Phone(True, True)

print(f'Can the phone call ?  {iphone.callingValue()}')
print(f'Can the phone sms ?  {iphone.smsValue()}')
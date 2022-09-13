# Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
# Phone Class.

#  10 . Write a python script to add the new method in SmartPhone class which accepts
# Truecaller object as a parameter and call the fetch method of Truecaller

from nine_25 import Truecaller
from five_six_25 import Calculator2
from seven_25 import Phone

class SmartPhone(Calculator2, Phone, Truecaller):
    
    def __init__(self):
        Calculator2.__init__(self)
        Phone.__init__(self)
        Truecaller.__init__(self)
        
    def knowCaller(self, caller):
        caller.fetchName(caller.number)
        
        
# Write a recursive python function to print first N odd natural numbers

def oddNaturalNumberGenerator(n):
    if n > 0:
        oddNaturalNumberGenerator(n-1)
        print( (2*n) -1)
        
        
oddNaturalNumberGenerator(5)
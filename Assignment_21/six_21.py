# Write a recursive python function to print first N even natural numbers in reverse
# order.

def evenNaturalNumberGenerator(n):
    if n > 0:
        print( (2*n))
        evenNaturalNumberGenerator(n-1)
        
evenNaturalNumberGenerator(5)
# Write a recursive python function to print first N even natural numbers.

def evenNaturalNumberGenerator(n):
    if n > 0:
        evenNaturalNumberGenerator(n-1)
        print( (2*n))

evenNaturalNumberGenerator(5)
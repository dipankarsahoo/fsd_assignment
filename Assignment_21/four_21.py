# Write a recursive python function to print first N odd natural numbers in reverse order

def oddNaturalNumberGenerator(n):
    if n > 0:
        print( (2*n) -1)
        oddNaturalNumberGenerator(n-1)

oddNaturalNumberGenerator(5)
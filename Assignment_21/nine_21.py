# Write a recursive python function to print first N multiples of a given number.

def numMultiples(n , num):
    if n > 0:
        numMultiples(n-1, num)
        print(n * num)
        
numMultiples(10, 5)
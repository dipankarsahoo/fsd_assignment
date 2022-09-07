# Create a generator to produce squares of first N natural numbers

def squareOfNaturalNumberGenerator(n):
    # Setting the range of numbers to count
    for i in range(1, n+1):
        # yield the square
        yield i * i

n= int(input("Enter the number of values needed:"))
for e in squareOfNaturalNumberGenerator(n):
    print(e)
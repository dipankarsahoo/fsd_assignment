# Create a generator to produce first n odd natural numbers

def oddNaturalNumberGenerator(n):
    # Setting the initial value of odd number
    a = 1
    for i in range(n):
        # yield the number in series
        yield a
        # set the next number in series
        a += 2

for e in oddNaturalNumberGenerator(int(input("Enter the number of values needed:"))):
    print(e)

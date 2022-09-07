# Create a generator to produce first n even natural numbers


def evenNaturalNumberGenerator(n):
    # Setting the initial value of even number
    a = 2
    for i in range(n):
        # yield the value 
        yield a
        # Set the value to next in series
        a += 2

for e in evenNaturalNumberGenerator(int(input("Enter the number of values needed:"))):
    print(e)

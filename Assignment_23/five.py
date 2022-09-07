# Create a generator to produce first n terms of Fibonacci series

def fibonacciGenerator(n):
    # a and b initially contain the first two elements of fibonacci series
    a, b = 0, 1
    for i in range(n):
        # generator yields the first element
        yield a
        # setting the values of a and b to point the next value in series
        a, b = b, a+b
    
for e in fibonacciGenerator(int(input("Enter the number of values needed:"))):
    print(e)
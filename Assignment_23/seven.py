# Create an endless iterator using generator method to produce terms of Fibonacci series

def fibonacciGenerator():
    # a and b initially contain the first two elements of fibonacci series
    a, b = 0, 1
    while True:
        # generator yields the first element
        yield a
        # setting the values of a and b to point the next value in series
        a, b = b, a+b

it = fibonacciGenerator()

fibo_list = []
while True:
    if input("Do you want to generate another element[y/n]") == 'y':
        a = next(it)
        print(a)
        fibo_list.append(a)
    else:
        break

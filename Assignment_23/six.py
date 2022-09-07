# Create a generator to produce first n prime numbers

def primeNumberGenerator(n):
    # Setting natural numbers count to 1
    number = 1
    while n:
        number += 1
        ctr = 0
        # Check for number is prime
        for j in range(2, number):
            if number % j == 0:
                ctr+=1
        if ctr == 0:
            n -= 1
            yield number
        
for e in primeNumberGenerator(int(input("Enter the number of values needed:"))):
    print(e)

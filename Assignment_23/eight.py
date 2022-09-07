# Create an endless iterator using generator method to produce Prime numbers

def primeNumberGenerator():
    # Setting natural numbers count to 1
    number = 1
    while True:
        number += 1
        ctr = 0
        # Check for number is prime
        for j in range(2, number):
            if number % j == 0:
                ctr+=1
        if ctr == 0:
            yield number
        
it = primeNumberGenerator()

prime_list = []
while True:
    if input("Do you want to generate another element[y/n]") == 'y':
        a = next(it)
        print(a)
        prime_list.append(a)
    else:
        break

# Define a function which calculates the HCF of two numbers.
# Define and apply a decorator to check wheather two given numbers are co-prime or not.

def hcf(a,b):
    num = min(a,b)
    
    while num:
        if a % num == 0 and b % num == 0:
            break
        else:
            num -= 1
    return num

def coprime(func):
    
    def inner(a, b):
        # Everything divides 0
        if hcf(a, b) == 1: 
            print('They are co-prime')
        else:
            print('They are not co-prime')
        return hcf(a, b)
    
    return inner
            

gcd_check = coprime(hcf)

a = int(input('Enter first number '))
b = int(input('Enter second number '))

print(f'HCF of the numbers is : {gcd_check(a, b)}')
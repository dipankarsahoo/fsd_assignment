# Define a function which calculates the HCF of two numbers.
# Define and apply a decorator to check wheather two given numbers are co-prime or not.

def coprime(func):
    
    def inner(a, b):
        # Everything divides 0
        if func(a, b) == 1: 
            print('They are co-prime')
        else:
            print('They are not co-prime')
        return func(a, b)
    
    return inner
    
@coprime
def hcf(a,b):
    num = min(a,b)
    
    while num:
        if a % num == 0 and b % num == 0:
            break
        else:
            num -= 1
    return num        

# gcd_check = coprime(hcf)

a = int(input('Enter first number '))
b = int(input('Enter second number '))

print(f'HCF of the numbers is : {hcf(a, b)}')
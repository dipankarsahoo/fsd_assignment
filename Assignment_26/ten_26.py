# # Write a python script to check whether a given number is prime or armstrong number
# using 2 different threads.

import concurrent.futures

def check_prime(num):
    prime = 0
    for i in range(2, num-1):
        if num % i == 0:
            prime += 1  
            
    if prime == 0:
        print(f'{num} is prime')
    else:
        print(f'{num} is NOT prime')
        
def check_armstrong(num):
    sum = 0
    k = num
    while k > 0:
        sum = sum + (k % 10)**3
        k = k // 10
    
    if sum == num:
        print(f'{num} is armstrong number')
    else:
        print(f'{num} is NOT armstrong number')
        
with concurrent.futures.ThreadPoolExecutor() as executor:
    checks = [check_prime, check_armstrong]
    nums = [153, 4, 2, 8]
    for check in checks:
        result = executor.map(check, nums)
        print(f'{executor.__dict__} started')
        
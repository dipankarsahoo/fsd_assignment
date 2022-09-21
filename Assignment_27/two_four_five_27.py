# Write a python script to create a ValueError
# Write a python script to handle a ValueError
# Write a python script to handle multiple Exception in one try

try:
    k = input('Enter a positive number: ')
    if int(k) < 0:
        raise ArithmeticError
    elif int(k) % 2 == 0:
        print('Its even number')
    else:
        print('Its odd number')
except ValueError:
    print('ValueError')
except Exception:
    print('Some Exception in try block')
    
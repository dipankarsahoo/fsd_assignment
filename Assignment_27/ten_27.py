# Write a python script to implemented a nested Try Except block

try:
    a = int(input('Input a positive integer'))
    try:
        if a < 0:
            raise ArithmeticError
        else:
            print(a)
    except ArithmeticError:
        print('Its not a positive number')    
except ValueError:
    print('Invalid input')
except Exception:
    print('Some exception is caught')
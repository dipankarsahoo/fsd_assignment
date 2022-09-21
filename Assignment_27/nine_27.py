# Write a python script to raise a ValueError.

try:
    a = int(input('Input a positive integer'))
    
    if a < 0:
        raise ValueError
    else:
        print(a)
    
except ValueError:
    print('Invalid input')
except Exception:
    print('Some exception is caught')

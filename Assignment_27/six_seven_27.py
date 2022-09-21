# Write a python script to create a calculator with 4 basic operations, and handle a
# maximum number of exceptions
# Write a python script to add a finally block for the above script
# Write a python script to implement try except and else block for division

def calculator():
    
    try:
        a = int(input('Input a valid integer'))
        b = int(input('Input another valid integer'))
        
        print(f'Sum of the two numbers is {a + b}')
        print(f'Difference between the two numbers is {a - b}')
        print(f'Product of the two numbers is {a * b}')
        print(f'Division of the two numbers is {a / b}')
    except TypeError:
        print(f'Invalid type error') 
    except ValueError:
        print(f'Invalid value error')
    except FloatingPointError:
        print(f'Invalid floating point error')
    except OverflowError:
        print(f'Invalid overflow error')
    except ZeroDivisionError:
        print(f'Invalid division error')
    else:
        print('You entered correct numbers for the calculator!')
    finally:
        print('End of try')
        
calculator()
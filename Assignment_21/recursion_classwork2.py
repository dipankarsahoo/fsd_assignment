# write a recursive function to print first n natural numbers

def print_natural_numbers(n):
    if n > 0:
        print_natural_numbers(n - 1)
        print(n)
        
print_natural_numbers(10)
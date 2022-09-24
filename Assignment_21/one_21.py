# Write a recursive python function to print first N natural numbers

def print_natural_numbers(n):
    if n > 0:
        print_natural_numbers(n - 1)
        print(n)
        
print_natural_numbers(10)
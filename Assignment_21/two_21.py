# Write a recursive python function to print first N natural numbers in reverse order

def print_reverse(n):
    if n > 0:
        print(n)
        print_reverse(n-1)
        
print_reverse(10)
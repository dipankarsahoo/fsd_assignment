# write a recursive function to calculate sum of squares of first n natural numbers.

def sum_of_squares(n):
    if n ==1:
        return 1
    else:
        return n**2 + sum_of_squares( (n-1) )
    
print(sum_of_squares(32))
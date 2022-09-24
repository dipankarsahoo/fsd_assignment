# Write a recursive python function to print a number in reverse order.

def reverseNum(n):
    if n > 0:
        print( n % 10, end='' )
        reverseNum( n // 10) 
        
reverseNum(2548)
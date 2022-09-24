# Write a recursive python function to print squares of first N natural numbers

def squareNum(n):
    if n > 0:
        squareNum(n - 1)
        print(n ** 2)
          
squareNum(5)
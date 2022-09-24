# Write a recursive python function to print cubes of first N natural numbers

def cubeNum(n):
    if n > 0:
        cubeNum(n - 1)
        print(n ** 3)
          
cubeNum(5)
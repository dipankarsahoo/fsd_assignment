# Define a function which takes lengths of three sides of a triangle as arguments and display the perimeter of triangle.
# Define and apply a decorator which checks for validity of the triangleon the basis of lengths of the sides of the triangle. This makes
# perimeter to be displayed when the triangle can exist.



def validateTraiangleSides(func):
    
    def inner(a, b, c):
        if a+b > c and b+c > a and a+c > b:
            return func(a, b, c)
    
    return inner

@validateTraiangleSides
def perimeterTriagnle(a, b, c):
    return a + b + c
      
# perimeter = validateTraiangleSides(perimeterTriagnle)

a = float(input('Enter length of one side of triangle'))
b = float(input('Enter length of second side of triangle'))
c = float(input('Enter length of third side of triangle'))

if perimeterTriagnle(a, b, c) != None:
    print(f'Perimeter of triangle ={perimeterTriagnle(a, b, c)}')
else:
    print('Wrong inputs for sides of a triangle')

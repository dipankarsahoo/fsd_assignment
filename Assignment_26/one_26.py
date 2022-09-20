# Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in
# a class using method overloading.

class MethodOverload:
    def multiply(self, *args):
        product =1
        for self.num in args:
            product *= self.num
            
        return product
    
overload = MethodOverload()

print( f'Multiply 4 numbers {overload.multiply(1, 2, 3, 4)}')
print( f'Multiply 3 numbers {overload.multiply(1, 0, 3)}')
print( f'Multiply 2 numbers {overload.multiply(1, 2.5)}')
print( f'Multiply 1 numbers {overload.multiply(-8)}')
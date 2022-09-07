# Use iter and next method to access all the elements of a given set using while loop

s = {1, 3, 4, 5, 6, 7, 8, 9, 'c', 4, 5, 7, 'k'}

it = iter(s)

while True:
    try:
        print(next(it))
    except StopIteration:
        pass
  
# this example prints the values c and k in arbitrary order when executed multiple times.  
# Write a python script to change the name of the Thread.

from threading import Thread

def even_100():
    for n in range(100):
        if n % 2 == 0:
            print(f'{n} is an even number')
            
def odd_100():
    for n in range(100):
        if n % 2 != 0:
            print(f'{n} is an odd number')


t1 = Thread(target=even_100)
t2 = Thread(target=odd_100)

t1.name = 'even_100'
t2.name = 'odd_100'

t1.start()
print(f'{t1.name} started  ')
t2.start()
print(f'{t2.name} started  ')

t1.join()
print(f'{t1.name} joined ')
t2.join()
print(f'{t2.name} joined  ')
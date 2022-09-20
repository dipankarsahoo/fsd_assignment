# Write a python script to create two Threads. First thread will print all Even numbers
# and Second thread will print all Odd numbers till 100

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

t1.start()
t2.start()

t1.join()
t2.join()

print('End of Threads')
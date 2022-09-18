from threading import Thread
import os
import time

def square(a):
    for i in range(100):
        i**2
        time.sleep(0.1)

threads = []
num_threads = 10

# create threads
for i in range(num_threads):
    t = Thread(target=square, args= (5,))
    threads.append(t)
    
# start process
k=1
for t in threads:
    t.start()
    print(f'Thread started {k}')
    k+= 1
    
# join
for t in threads:
    t.join()
    
print("Ended")
from multiprocessing import Process
import os
import time

'''This program gives error on windows machine check below for more info
https://stackoverflow.com/questions/18204782/runtimeerror-on-windows-trying-python-multiprocessing'''
  
def square(a):
    for i in range(100):
        i**2
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

# create processes
for i in range(num_processes):
    p = Process(target=square, args= (5,))
    processes.append(p)
    
# start process
k=1
for p in processes:
    p.start()
    print(f'Process started {k}')
    k+= 1
    
# join
for p in processes:
    p.join()
    
print("Ended")
# Write a python script to create 5 threads to fill a list with random numbers till 100.

import concurrent.futures
import random

l= []
def fill_random(n):
    partition = [i for i in range((20 * (n-1)), (20 * n))]
    random.shuffle(partition)
    for i in partition:
        l.append(i)
        
    if len(l)==100:
        print(l)
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    t_count = [i for i in range(1,6)]
    results = executor.map(fill_random, t_count)
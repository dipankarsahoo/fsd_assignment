# Write a python script to create 2 threads to add all the values from 1 to 100.

import concurrent.futures

def add_input_to_sum():
    sum = 0
    for i in range(101):
        sum += i
    print(sum)
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(2):
        print(executor._thread_name_prefix)
        f = executor.submit(add_input_to_sum)
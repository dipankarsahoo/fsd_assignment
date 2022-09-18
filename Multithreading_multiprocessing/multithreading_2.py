from threading import  Thread
import time

start = time.perf_counter() 

def do_something(seconds): 
    print(f'Sleeping for {seconds} now')
    time.sleep(seconds)
    print('Done sleeeping...')
    
threads = []    

for _ in range(100):
    t = Thread(target=do_something, args=[1.5])
    t.start()
    print(t.getName())
    threads.append(t)
    
for thread in threads:
    thread.join()
    
finish = time.perf_counter()

print(f'Sleeping for {round(finish-start, 2)} seconds')
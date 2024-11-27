import time
from threading import Thread
import random



results = []
def claculateThePi(n,index):
    i=0
    for _ in range(n):
        x= random.uniform(-1,1)
        y= random.uniform(-1,1)
        r= x**2 + y**2
        
        if (x**2+y**2) <=1:
            i+=1
    #storing the values in the array
    results[index] = i

def estimate_pi(n, num_threads=16):
    global results
    points_per_thread = n // num_threads
    #Using buffer to store the each result from the thread
    results = [0]*num_threads
    threads = []
    #Creating Number of threads
    for i in range(num_threads):
        t = Thread(target=claculateThePi,args=(points_per_thread,i))
        threads.append(t)
        t.start()
    #joining al the threads
    for j in threads:
        j.join()
    #Sum all the i which are result from the threads 
    total_result = sum(results)
    #The result 
    pi = 4 * total_result/n

    return pi

start_time = time.time()
n=10000000
pi = estimate_pi(n)
end_time = time.time()
elapsedtime = end_time - start_time 
print(pi,"The elapsed Time :",elapsedtime)


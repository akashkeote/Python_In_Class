import time 
start = time.time()

arr1= [i for i in range(100000000)]
brr = [i for i in range(100000000,200000000)]


print(time.time()-start) #5.4 sec


import numpy as np 
start = time.time()
a = np.arange(100000000)
b = np.arange(100000000,200000000)
print(time.time()-start) # 0.2sec
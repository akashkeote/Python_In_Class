import numpy as np
arr = np.array([[1,2,3,4,5],[5,4,3,2,1]])
print(arr[0])
print(arr[1])
print(arr[0][1])
print(np.int64(2)) #internally issa output ayega

print(arr[0,1]) #yeh bhi same output ayega

arr_new = np.array([[1,2,3,4,5],[5,4,3,2,1]])
print(arr_new[0,-1]) #-1 bole to last se value start hoti hai yaha par 
print(arr_new[-1])
arr_new[-1]=[7,7,7,7,7]
print(arr_new[-1])

arr_new[-2]=8
print(arr_new[-2])
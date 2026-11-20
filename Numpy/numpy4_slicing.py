import numpy as np 
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr)
print(arr[:])
#yaha 1d hi hoga bas 
print(arr[0:1]) # 1st row
#2-d hoga yaha 
print(arr[0:4,0:4]) #1st and 2nd row
     #RANGE:ROW/COLUMN limit

print(arr[0:1,3:]) #1st row and 

brr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])
print(brr[:])
print(brr[0:5:2,0:4:2]) #1st and 3rd row and 1st and 3rd column

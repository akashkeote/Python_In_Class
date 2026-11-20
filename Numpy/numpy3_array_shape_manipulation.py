import numpy as np
arr  = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr)
reshaped = arr.reshape(3,4)
ak = np.reshape(arr,(3,4))
#Notes - if i give 3,3 or 2,2 it show error because 3x4 = 12 
# and 3x3 = 9 and 2x2 = 4 
# so it is not possible to reshape it to that shape
print(reshaped)
print(ak)

#flattern vs ravel 
flatten = reshaped.flatten()
flatten[0]=7
print("Before Flatten")
print(reshaped)
print('After Flatten')
print(flatten)

ravel = reshaped.ravel()
ravel[0]=9
print("Before ravel")
print(reshaped)
print("After Ravel")
print(ravel)




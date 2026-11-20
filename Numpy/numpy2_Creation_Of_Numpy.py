import numpy as np
numpy_array = np.array([1,2,3])
print(numpy_array)
#array is better in processing than list 
#2-d array
two_d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(two_d)

print(two_d.dtype) #int64

print(two_d.shape) #(3,3)

print(two_d.size) # 3x3 = 9

print(two_d.ndim) #2      2 dimentsion hai ye

#array with zeros values
zeros = np.zeros((2,3))
print(zeros) #[[0. 0. 0.]
#              [0. 0. 0.]]

#but you got the float values
print(zeros.dtype) #float 64


#now i want all of them as int 
ak = np.ones((3,3),dtype=int)
print(ak) #3x3 array hai ye to 
print(ak.dtype) #int64

bk = np.arange(11)
print(bk) #[ 0  1  2  3  4  5  6  7  8  9 10]

ck = np.arange(0,6,0.5) #start stop step
print(ck) #[0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5 5. ]


#equal distributed values between start and stop
#stop is included in the values in linspace
dk = np.linspace(1,5,10) #start stop number of values
print(dk) #[1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222


#numpy array shape manipulation using reshape ravel and flatten
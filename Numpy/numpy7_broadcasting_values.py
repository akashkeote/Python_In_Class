import numpy as np

arr1 = np.array([[1, 2, 4], 
                 [4, 5, 6]])
print(arr1)
print(arr1 + 4)
print(arr1 + np.array([5, 6, 7]))
print(arr1 + np.array([[1],
                        [2]]))
import numpy as np
day_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
steps_walked = [6012, 7079, 6886, 7230, 4598, 5564, 6971, 7763, 8032, 9569]
#i want to create a numpy array with these two lists as columns. How can I do that?
# day_number[0]with steps_walked[0] as the first row, day_number[1] with steps_walked[1] as the second row, and so on. You can use the numpy library to create a 2D array (matrix) where each list becomes a column. Here's how you can do it:


data = np.column_stack((day_number, steps_walked))
print(data)
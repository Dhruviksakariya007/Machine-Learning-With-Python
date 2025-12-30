import numpy as np

arr = np.array([1,2,3,4,5,6])

# start(included), stop(excluded), step
print(arr[:5:2])
print(arr[-1:-5:-1])


# reshaped array
# 1d array into multi diamensional array! but total elements must be same.
print(arr.reshape(2,3))  # 2 rows, 3 columns

print('\n')
# multidimensional array into 1d array 
# both works same
# .ravel -> view - don't affact to original array
# .flatten -> copy - affact to original array
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())
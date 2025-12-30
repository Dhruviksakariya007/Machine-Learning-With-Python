import numpy as np

arr = np.array([10, 20, 30])
arr2 = np.array([[10,20,30], 
                 [40,50,60]])

print(arr)
print(arr2,'\n')

print(arr[0])
print(arr[-1], '\n')

# first row, third column 
# [0,1] [1,2,3] [4,5,6]  ---  [0,1] 0 -> [1,2,3], 1 -> [4,5,6] -> [0,1] -> 2 # same gose to [1,2] -> 6
print(arr2[1,2], '\n')

# fancy indexing -> similar to slicing
arr_fancy = np.array([1,2,3,4,5,6,7,8,9])
print(arr_fancy[[0,2,3]])
# 1, 3, 4
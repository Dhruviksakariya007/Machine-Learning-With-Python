"""
np.insert(array, index, value, axis=None(optional))
axis=None -> flatened array (1d)
axis=0 -> rows -
axis=1 -> columns |
"""
import numpy as np

arr = np.array([1,2,3,4,5,6])
arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[4,5,6]])

print(np.insert(arr, 1, 10), '\n') # insert 10 at index 1

print(arr2, '\n')
print(np.insert(arr2, 2, [5,6,7], axis=0), '\n') # insert [5,6,7] as new row at index 2
print(np.insert(arr2, 2, 5, axis=1), '\n') # insert 5 in all rows at index 2

# appand values at the end

print(np.append(arr, 9), '\n') # print(np.append(arr, [7,8,9]), '\n')

print(np.concatenate((arr, arr1)), '\n') # concatenate two arrays

# np.delete(array, index, axis=None(optional))
print(np.delete(arr, 2), '\n') # delete element at index 2 -> value 3
print(arr2, '\n')
print(np.delete(arr2, 1, axis=1), '\n') # axis is mandatory for multi-dimensional arrays


# Stacking arrays
# stack arrays used to stack vertically or horizontally
# vstack -> vertical stack
# hstack -> horizontal stack
vstack_arr = np.vstack((arr2,arr2))
print("VStack Multidiamension array: \n", vstack_arr, '\n') # vertical stack
print(arr2)
print(np.hstack((arr2)), '\n') # horizontal stack

# splitting arrays
# split array into multiple sub-arrays
# split(), hsplit(), vsplit()
print(np.split(arr, 3), '\n')
print(np.hsplit(arr, 2), '\n')
print(np.vsplit(arr2, 2), '\n')
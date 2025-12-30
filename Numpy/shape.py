# when working with multi-dimensional data shape used to identify structure of it! (matrix)
# use for identifying structute of the data! returns numbers of dimentions
# All about checking!

import numpy as np

array_1d = np.array([1,2,3])
array_2d = np.array([[1,2,3],
                    [4,5,6]])
array_str = np.array([1,2,3, 4.5, 'hello'])
array_U = np.array([1.2,3.2,3.4])


print(array_2d.shape, '\n') # Structure of matrix

print(array_2d.size, '\n') # returns size of whole matrix

# returns dimensions of matrix 1d, 2d, 3d
print(array_1d.ndim, '\n') 
print(array_2d.ndim, '\n') 

# returns datatype! element's datatype
print(array_str.dtype, '\n')

# changing datatypes
# text -> numbers
# type conversion
print("Matrix : ", array_U, '\n')
print(array_U.dtype, '\n')
change_datatype = array_U.astype(int)
print(change_datatype, '\n')
print(change_datatype.dtype, '\n')

# e.g
str = np.array("12345")
str_int = str.astype(int)
print(str_int)

l = [1,2,3]
new_l = []
for i in range(len(l)):
    new_l 
    new_l.append(l[i] * 2)
    print(new_l)
    
print('\n', new_l)
# better way
l = [1,2,3]
new_l = [i * 2 for i in l]
print(new_l)

# more efficient way using numpy
array = np.array([1,2,3])
new_array = array * 2
print(new_array, '\n')

# aggrigaition fuction / summary -> min, max, standard deviation, varience, mean
print("Sum: ", np.sum(array_1d), '\n') # sum of all elements
print("Max: ", np.max(array_1d), '\n') 
print("mean: ", np.mean(array_1d), '\n') 
print("Min: ", np.min(array_1d), '\n') 
print("Standard Deviation: ", np.std(array_1d), '\n') 
print("Var: ", np.var(array_1d), '\n')
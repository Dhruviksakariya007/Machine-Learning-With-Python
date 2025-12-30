# Error in different diamensions operations 
# broadcasting used to perform operations on different diamensions arrays + - ... ect
import numpy as np

arr = np.array([100, 200, 300])
arr2 = np.array([10, 20, 30])
arr3 = np.array([[10, 20, 30],
                 [40, 50, 60]])

descounred = arr - (arr  * 10 / 100 )
print(descounred.astype(int), '\n')  # converting float to int

print(arr2 + arr3, '\n')  # addition
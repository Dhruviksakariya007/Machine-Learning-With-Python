# Learning NumPy

import numpy as np
import scipy.stats as sp

data = [50, 70, 70, 45, 76, 99, 88]

print("Mean:", np.mean(data)) # avarage
print(f"median: {np.median(data)}")
print(f"mode: {sp.mode(data)}")



matrix = np.array([[1,4,6], [8,9,12]])
print(matrix, '\n')

# Always give diamension in tuple!  
print(np.zeros(4),'\n') # array of 4 zeros // like default values in the matrix
print(np.ones(4),'\n') # default values '1'
print(np.ones((3,4)), '\n') # 3x4 matrix of ones
print(np.full((2,2),7), '\n') # array of 3 elements with default value 7

print(np.arange(1,10,2), '\n') # array from 1 to 9 with the difference of 2 

randomMatrix = np.random.rand(3,2) # 3x3 matrix with random values between 0 and 1
print(randomMatrix, '\n')

print(np.eye(3), '\n') # identity matrix of 3x3
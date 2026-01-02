import numpy as np
arr = np.array([10,20,30,40,53,60])
name = np.array(['apple', 'banana', 'cherry', 'date'])

print(arr, '\n')

print(np.where(arr == 30), '\n')
print(np.where(arr%2 == 0), '\n')
print(np.where(arr%2 == 1), '\n')


# searchsorted() to search something from the array!
print(np.searchsorted(arr, 53), '\n')
print(np.searchsorted(arr, [100]), '\n') # if the value is not found, it will return the index where it should be inserted to maintain order
print(np.searchsorted(name, 'cherry'), '\n')
print(np.searchsorted(name, 'cherry', side='right'), '\n') # return the index number from right side!


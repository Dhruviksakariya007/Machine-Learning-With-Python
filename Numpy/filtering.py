# boolean filtering
# more efficient way of filtering data in numpy arrays
# faster than loops 
# can praform operations!

import numpy as np

arr = np.array([1,2,3,4,5])

print(arr[arr>2]) 

print(arr[arr%2 == 0])  # even numbers


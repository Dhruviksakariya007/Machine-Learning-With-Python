import numpy as np

a = np.array([1,2,np.nan,4,5])

# detect missing values
print(np.isnan(a))  # check for nan values

# nan is not equal to nan
# we can not compare nan with anything including nan itself!
# we only can fine nan values using np.isnan()
print(np.nan == np.nan)

# nan_to_num(array, nan=VALUES) -> convert nan to number
# this function used to handle missing values with custome or default values
print(np.nan_to_num(a)) # Default nan=0
print(np.nan_to_num(a, nan=-1)) # custom value for nan


# isinf() -> check for infinite values
# a number which is too large to be represented in that dataset or 1/0
# isinf() is to find infinite values
a_inf = np.array([1,2,3, np.inf, -np.inf])
print(np.isinf(a_inf))

# replace inf value
print(np.nan_to_num(a_inf, posinf=1000, neginf=-1000)) 

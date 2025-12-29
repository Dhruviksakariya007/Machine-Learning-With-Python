import numpy as np
import scipy.stats as sp

data = [50, 70, 70, 45, 76, 99, 88]

print("Mean:", np.mean(data))
print(f"median: {np.median(data)}")
print(f"mode: {sp.mode(data)}")

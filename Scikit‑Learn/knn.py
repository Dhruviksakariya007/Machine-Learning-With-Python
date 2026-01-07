# it makes decision based on nearest neighbors - mejority!
# works well with small data sets
# not required complex Maths
from sklearn import *
from sklearn.linear_model import *
from sklearn.neighbors import *
import pandas as pd

data = {
    "Weight":[ [180, 7],
               [200, 7.5],
               [250, 8],
               [300, 8.5],
               [330, 9],
               [360, 9.5]],
# 0 - Apple, 1 - Orange
 "Name": [0, 0, 0, 1, 1, 1, 1]
}
# df = pd.DataFrame(data)

Weight = float(input("Enter Weight: "))
Size = float(input("Enter Size: "))

input = [ [180, 7],
               [200, 7.5],
               [250, 8],
               [300, 8.5],
               [330, 9],
               [360, 9.5]]

output = [0, 0, 0, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)

model.fit(input, output)

predictions = model.predict([[Weight, Size]])[0] # [0] or [1] - 0 means value inside list and 1 returns whole list

if predictions == 1:
    predictions = "Orange"
else:
    predictions = "Apple"

print(f"Based on your weight ({Weight}) and size ({Size}), the predicted fruit is '{predictions}'")
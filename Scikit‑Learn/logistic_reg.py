from sklearn import *
from sklearn.linear_model import *
import pandas as pd

data = {
    'StudyHours': [2, 3, 5, 1, 4, 6, 8, 7],
    'Result': [0, 0, 1, 0, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

hr = float(input("Enter your Studied Hours: "))

input = df['StudyHours'].values.reshape(-1, 1)
output = df['Result']

model = LogisticRegression()
model.fit(input, output)

predictions = model.predict([[hr]]) # [0] or [1] - 0 means value inside list and 1 returns whole list

if predictions == 1:
    predictions = "Pass"
else:
    predictions = "Fail"
print(f"Based on your hours ({hr}) you may score around {predictions}")
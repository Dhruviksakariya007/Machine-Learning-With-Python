from sklearn import *
from sklearn.linear_model import *
import pandas as pd

data = {
    'StudyHours': [2, 3, 5, 1, 4, 6, 8, 7],
    'TestScores': [50, 60, 80, 40, 70, 90, 95, 85]
}
df = pd.DataFrame(data)

hr = float(input("Enter your Studied Hours: "))

input = df['StudyHours'].values.reshape(-1, 1)
output = df['TestScores']

model = LinearRegression()
model.fit(input, output)

predictions = model.predict([[hr]])[0] # [0] or [1] - 0 means value inside list and 1 returns whole list

print(f"Based on your hours ({hr}) you may score around {predictions}")
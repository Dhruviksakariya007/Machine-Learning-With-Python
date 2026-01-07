from sklearn.metrics import *
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

data = pd.read_csv('/Users/mac/Documents/Machine Learning/Scikit‑Learn/stud.csv')

x = data[['Hours']]
y = data['Score']

l = LinearRegression()
l.fit(x, y)
predict = l.predict(x)

mse = mean_squared_error(y, predict)
mae = mean_absolute_error(y, predict)
Rmse = np.sqrt(mse)

print(predict)
print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("Root Mean Squared Error:", Rmse)

print(sum([0, 0.9, 1.2, 0.3, 0.6])/5)
mse_calc = sum([0, 0.9*0.9, 1.2*1.2, 0.3*0.3, 0.6*0.6])/5
print(mse_calc)
print(np.sqrt(mse_calc))

# uinput = float(input("Enter study hours: "))
# predicted_score = l.predict([[uinput]])
# print(f"Predicted Score for studying {uinput} hours: {predicted_score[0]}")

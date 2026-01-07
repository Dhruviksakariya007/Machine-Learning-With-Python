# MAE - mean absolute error means how far is my model predicts from actual values
# MSE - mean squared error means square(2x) of the difference between actual and predicted values 
# difference between actual and predicted values is 5 then it will be 25 (5x5) and after that average of all the values
# RMSE - root mean squared error is square root of mse
# R^2 - how well the model predictions are matching with actual values
# 1.0 means perfect match
# 0.0 means no match at all
# <0.0 means worse than no match at all
import numpy as np
from sklearn.metrics import *

true_ans =  [90, 60, 80, 100]
predicted_ans = [85, 70, 70, 95]

mae = mean_absolute_error(true_ans, predicted_ans)
mse = mean_squared_error(true_ans, predicted_ans)
# no specific method for RMSE in sklearn, so we calculate it manually
rmse = np.sqrt(mse)
R2 = r2_score(true_ans, predicted_ans)

# when you need simple ans like on an average how much the model is wrong! use MAE
# simple to explain
print(f"Mean Absolute Error (MAE) Avg mistake values: {mae}")
# when you want to analyse some big mistakes! use MSE 
# when you need to find outlier mistakes
print(f"Mean Squared Error (MSE) Square of mistake values: {mse}")
# what is the error or mistake on real units!
# housing price, health, exam marks
print(f"Root Mean Squared Error (RMSE) Square root of mse: {rmse}")
print(f"R^2 Score (R2) How well the model predictions match actual values: {R2}")
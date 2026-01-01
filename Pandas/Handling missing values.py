# NaN
# None (for object datatypes)

# isnull() to check the missing values!
import pandas as pd
import numpy as np

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000,52000, 49000, 70000, 48000,None],
    "Performance_Score": [85, 90, 75, 80, None, 95, 78, 87]
}

df = pd.DataFrame(data)

print(df, '\n')

# filling missing values, set default value or mean/median/mode etc.
# df.fillna(0, inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df, '\n') 

print(df.isnull().sum(), '\n') 

df.dropna(inplace=True) # axis=0 for rows (default), axis=1 for columns
print(df, '\n')


# filling estimated values at missing value!
# interpolation
# it predict the missing values based on other values!
# avoid data loss!
# 3 main methonds: linear, polynomial, time
# df.interpolate(method="linear", inplace=True)
# print(df, '\n')
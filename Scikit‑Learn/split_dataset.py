# standardscaler used to scale features such that they have mean=0 and variance=1
# means that features will be centered around 0 with standard deviation of 1
# because features with different scales/values/numbers can negatively impact model performance

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import *

data = {
    'StudyHours': [2, 3, 5, 1, 4, 6, 8, 7],
    'TestScores': [50, 60, 80, 40, 70, 90, 95, 85]
}

df = pd.DataFrame(data)
print(df, '\n')

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df) # means and std deviation will be calculated for each column separately and scaling will be done accordingly
scaled_df = pd.DataFrame(scaled_data, columns=df.columns) # columns=df.columns to retain original column names otherwise it will be 0,1
print(scaled_df, '\n')

MinMaxScaler = MinMaxScaler()
minmax_scaled_data = MinMaxScaler.fit_transform(df)
minmax_scaled_df = pd.DataFrame(minmax_scaled_data, columns=df.columns)
print(minmax_scaled_df, '\n')


# train_test_split
input = df['StudyHours']
output = df['TestScores']

# random state means you will get same split! every time you run the code
x_tain, x_test, y_train, y_test = train_test_split(input, output, test_size=0.8, random_state=42) # random_state is used to get same split every time you run the codes

print("X_train:\n", x_tain, '\n')
print("X_test:\n", x_test, '\n')
print("Y_train:\n", y_train, '\n')
print("Y_test:\n", y_test, '\n')

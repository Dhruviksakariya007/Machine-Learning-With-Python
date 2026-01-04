# helps to conver text into numerical values so that model can understand!
from sklearn.preprocessing import *
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np

df = pd.read_csv('/Users/mac/Documents/Machine Learning/Scikit‑Learn/student-mat.csv')

print(df.head())

le = df.copy()

le_Encoder = LabelEncoder()

# le['NEW_NAME'] = le_Encoder.fit_transform(le['EXISTING_NAME'])
le['Gender'] = le_Encoder.fit_transform(le['sex'])
# print(le.columns)
print(le[['school', 'sex', 'Gender']].head())

# with this encoding, 'F' will be converted to 0 and 'M' to 1, model can understand these numerical values and train accordingly!

df.replace({'Pstatus': {'A': 0, 'T': 1}}, inplace=True)
print(df.head())


# *******************************
# One Hot Encoding
# *******************************
df_encoded = pd.get_dummies(df, columns=['school'])
print(df_encoded.head())

# standardscaler used to scale features such that they have mean=0 and variance=1
# means that features will be centered around 0 with standard deviation of 1
# because features with different scales/values/numbers can negatively impact model performance
scaler = StandardScaler()
scaled = scaler.fit_transform(df[['age', 'absences', 'G1', 'G2', 'G3']])
print(scaled, '\n')

minmax_scale = MinMaxScaler()
minmax_scaled = minmax_scale.fit_transform(df[['age', 'absences', 'G1', 'G2', 'G3']])
print(minmax_scaled)
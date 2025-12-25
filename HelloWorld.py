import pandas as pd

dataSet = pd.read_csv('vgsales.csv')
print(dataSet.shape)
print(dataSet.describe())
print(dataSet.head())

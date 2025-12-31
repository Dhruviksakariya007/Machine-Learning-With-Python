import pandas as pd

# read_excel(PATH)
df = pd.read_csv('music.csv')

print(df.head(10)) # shows first 10 rows
print(df.tail(10)) # shows last 10 rows

print('\n')

print(df.info(), '\n') # shows summary of dataframe
print(df.describe(), '\n') # shows statistical summary of data

print(df.columns, '\n') # shows column names
print(df.shape, '\n') # shows number of rows and columns
print(df.dtypes, '\n') # shows data types of each column

multi_cols = df[["age", "gender"]]
print(df["age"], '\n')
print(multi_cols, '\n')

# sorting / filtering
sorted_by_salary = df[(df["age"] == 30) | (df['age'] == 34)]
print(sorted_by_salary, '\n')

# to save file as .csv
# default index=True which also saves the index column
df.to_csv('music_copy.csv', index=False) 

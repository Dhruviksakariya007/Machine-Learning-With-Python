import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000,52000, 49000, 70000, 48000,None],
    "Performance_Score": [85, 90, 75, 80, None, 95, 78, 87],
    "Time": [1, 2, 3, 4, 5, None, 7, 8]
}

df = pd.DataFrame(data)


# filling estimated values at missing value!
# interpolation
# it predict the missing values based on other values!
# avoid data loss!
# 3 main methonds: linear, polynomial, time
# can only work with numerical data
df.interpolate(method="linear", inplace=True)
print(df, '\n')

# df.interpolate(method="time", inplace=True)
# print(df, '\n') 
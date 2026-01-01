import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 22, 32],
    "Salary": [50000, 60000, 45000,52000, 49000, 70000, 45000,58000],
    "Performance_Score": [85, 90, 75, 80, 82, 95, 78, 87]
}

df = pd.DataFrame(data)
print(df, '\n')

# grouped = df.groupby('Age')['Salary'].agg(sp.mode)
# grouped = df.groupby('Age')['Salary'].sum()
grouped = df.groupby(['Age', 'Name'])['Salary'].sum()
print(grouped, '\n')
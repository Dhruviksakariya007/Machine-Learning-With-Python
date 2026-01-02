import sys
import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000,52000, 49000, 70000, 48000,58000],
    "Performance_Score": [85, 90, 75, 80, 82, 95, 78, 87]
}

df = pd.DataFrame(data)

print(df, '\n')

# Adding a new column at the end
df["Bonus"] = df['Salary'] * 0.1
print(df, '\n')

# using insert methond which used to add column at specific location
df.insert(0, "Employee_ID", [1,2,3,4,5,6,7,8])
print(df, '\n')

# updating values in column
# .loc[]
df.loc[0, "Salary"] = 52000
df.loc[7, "Performance_Score"] = 90
print(df, '\n')

# same 👆🏻
df["Salary"] = df["Salary"] * 1.05
print(df, '\n')

# removing columns
# inpace=True modifies the original dataframe (Mendatory)
df.drop(columns=["Bonus", "Age"], inplace=True)
print(df, '\n')


# sorting values
print(df.sort_values(by=["Salary", "Performance_Score"], ascending=False), '\n') # [false, true] but it's not working! don't know why!

# resetting index
df.reset_index(inplace=True) # df.reset_index(drop=True, inplace=True)
print(df, '\n')

# drop duplicate rows
print(df.drop_duplicates(), '\n')

df.plot(kind='bar', x='Name', y='Salary', title='Employee Salary')
import matplotlib.pyplot as plt
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()
# plt.show()

# replace
df.replace({"Ram": "Rama"}, inplace=True)
print(df, '\n')

df.replace(['Shyam', 'Simran'], ['Shyamu', 'Simar'], inplace=True)
print(df, '\n')
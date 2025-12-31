# NaN
# None (for object datatypes)

# isnull() to check the missing values!
import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000,52000, 49000, 70000, 48000,58000],
    "Performance_Score": [85, 90, 75, 80, 82, 95, 78, 87]
}

df = pd.DataFrame(data)

print(df, '\n')
# H.W.
# 1. customer profile and 2. customer transaction
# merge customer and cancate in another dataframe

import pandas as pd

customer_profile = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [28, 34, 29, 42]
})

customer_Transaction = pd.DataFrame({
    'CustomerID': [1, 2, 3, 5],
    'TransactionAmount': [250, 450, 300, 500]
}) 

print("Customer Profile DataFrame:\n", customer_profile, '\n')
print("Customer Transaction DataFrame:\n", customer_Transaction, '\n')

merged_df = pd.merge(customer_profile, customer_Transaction, on='CustomerID', how='outer')
print("Merged DataFrame (Inner Join):\n", merged_df, '\n')

concate0 = pd.concat([customer_profile, customer_Transaction], axis=0, ignore_index=True)
concate1 = pd.concat([customer_profile, customer_Transaction], axis=1, ignore_index=False)

print(concate0, '\n')
print(concate1, '\n')

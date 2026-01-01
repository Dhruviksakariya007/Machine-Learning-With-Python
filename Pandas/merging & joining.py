# merging and concatenating
# combine multiple dataframes who share rows common key columns
import pandas as pd
import numpy as np

df_customers = pd.DataFrame({
    'CustomerID': [1,2, 3],
    'Name': ['Ramesh', 'Suresh', 'Kalpesh']
})

df_orders = pd. DataFrame ({
    'CustomerID': [1,2,4],
    'OrderAmount': [250, 450, 350]
})

# inner means shows only common rows
# outer means hows all rows but fills NaN for missing values
# cross means cartesian product of both dataframes (i don't understand properly!)
df_mergerd = pd.merge(df_customers, df_orders, on='CustomerID', how='inner')
print(df_mergerd, '\n')

# concatenation
# default axis=0 means rows (Vertical
# axis=1 means columns (Horizontal)
print(pd.concat([df_customers, df_orders], axis=0, ignore_index=True), '\n')

print(pd.concat([df_customers, df_orders], axis=1), '\n')

# H.W.
# 1. customer profile and 2. customer transaction
# merge customer and cancate in another dataframe
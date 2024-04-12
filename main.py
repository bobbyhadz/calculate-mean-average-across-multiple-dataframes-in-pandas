# Pandas: Calculate mean (average) across multiple DataFrames

import pandas as pd

df1 = pd.DataFrame({
    'x': [2, 4, 6, 8, 10],
    'y': [1, 3, 5, 7, 9]
})

df2 = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [6, 7, 8, 9, 10]
})

df3 = pd.concat([df1, df2])

print(df3)

print('-' * 50)

print(df3.mean())
import pandas as pd
import numpy as np
data = {
'Age': [21, 22, np.nan, 24, 25],
'Salary': [20000, np.nan, 25000, 30000, 28000]
}
df = pd.DataFrame(data)
print('Before Handling Missing Values:')
print(df)
# Replace missing Age with mean and Salary with median
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
print('After Handling Missing Values:')
print(df)
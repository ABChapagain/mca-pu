import pandas as pd
# Sample dataset
data = {
'Name': ['Ram', 'Sita', 'Hari', 'Gita'],
'Age': [21, 22, None, 23],
'Marks': [80, 85, 78, None]
}
df = pd.DataFrame(data)
print('Original Dataset:')
print(df)
print('Dataset Information:')
print(df.info())
print('Missing Values:')
print(df.isnull().sum())
# Fill missing values using mean
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
print('Preprocessed Dataset:')
print(df)
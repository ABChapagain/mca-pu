import pandas as pd
# students.csv is present in the same folder
# Columns: Hours, Marks, Attendance
df = pd.read_csv('students.csv')
print('First five records:')
print(df.head())
print('Summary Statistics:')
print(df.describe())
print('Dataset Shape:', df.shape)
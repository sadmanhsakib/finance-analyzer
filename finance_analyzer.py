import pandas as pd

# loading the dataset
df = pd.read_csv("transaction.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.shape)

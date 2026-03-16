import pandas as pd

# loading the dataset
df = pd.read_csv("transaction.csv")

# converting date column to datetime
df["date"] = pd.to_datetime(df["date"])

# standardize text columns to title case
df["category"] = df["category"].str.strip().str.title()
df["account_type"] = df["account_type"].str.strip().str.title()

# filling missing values
df["category"] = df["category"].fillna("Unknown")

# dropping rows where description is missing
df = df.dropna(subset=["description"])

# removing duplicate rows
df = df.drop_duplicates()

df.to_csv("cleaned_transactions.csv", index=False)
print("Cleaned data saved to cleaned_transactions.csv")

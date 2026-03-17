import pandas as pd

# loading the dataset
df = pd.read_csv("cleaned_transactions.csv")


def main():
    filter_data()


def clean_data():
    global df

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


def filter_data():
    global df

    # converting date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # extracting month
    df["month"] = df["date"].dt.month

    income_df = df[df["amount"] > 0]
    expense_df = df[df["amount"] < 0]
    expense_df["is_large"] = expense_df["amount"].abs() > 100

    print(df.head())


def export_data():
    df.to_csv("cleaned_transactions.csv", index=False)
    print("Cleaned data saved to cleaned_transactions.csv")


main()

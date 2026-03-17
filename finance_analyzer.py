import pandas as pd

# loading the dataset
df = pd.read_csv("cleaned_transactions.csv")


def main():
    export_data()


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
    # converting date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # extracting month
    df["month"] = df["date"].dt.month

    income_df = df[df["amount"] > 0]
    expense_df = df[df["amount"] < 0]
    expense_df["is_large"] = expense_df["amount"].abs() > 100

    print(df.head())


def analysis():
    global df

    # total spending per category
    expenses_df = df[df["amount"] < 0]
    expenses_df["amount"] = expenses_df["amount"].abs()
    spending_by_category = (
        expenses_df.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    spending_by_category.columns = ["category", "expenses"]

    # total income per month
    income_df = df[df["amount"] > 0]
    income_df["date"] = pd.to_datetime(income_df["date"])
    income_df["month"] = income_df["date"].dt.month_name()

    income_by_category = (
        income_df.groupby("month")["amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    income_by_category.columns = ["month", "income"]

    # total expenses  per month
    expenses_df = df[df["amount"] < 0]
    expenses_df["amount"] = expenses_df["amount"].abs()
    expenses_df["date"] = pd.to_datetime(expenses_df["date"])
    expenses_df["month"] = expenses_df["date"].dt.month_name()

    expenses_by_category = (
        expenses_df.groupby("month")["amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    expenses_by_category.columns = ["month", "expenses"]

    monthly_summary = pd.merge(
        income_by_category, expenses_by_category, on="month", how="outer"
    )
    monthly_summary["net_savings"] = (
        monthly_summary["income"] - monthly_summary["expenses"]
    )

    print(monthly_summary)


def export_data():
    expenses_df = df[df["amount"] < 0]
    expenses_df["amount_abs"] = expenses_df["amount"].abs()
    expenses_df["date"] = pd.to_datetime(expenses_df["date"])
    expenses_df["month"] = expenses_df["date"].dt.month_name()

    # pivot table - spending by category and month
    pivot = expenses_df.pivot_table(
        values="amount_abs",
        index="category",
        columns="month",
        aggfunc="sum",
        fill_value=0,
    )

    income_df = df[df["amount"] > 0]
    income_df["date"] = pd.to_datetime(income_df["date"])
    income_df["month"] = income_df["date"].dt.month_name()

    # pivot table - income by description and month
    income_pivot = income_df.pivot_table(
        values="amount",
        index="description",
        columns="month",
        aggfunc="sum",
        fill_value=0,
    )

    # building a clean final summary
    total_income = income_df["amount"].sum()
    total_expenses = expenses_df["amount_abs"].sum()
    net_savings = total_income - total_expenses
    savings_rate = (net_savings / total_income) * 100

    summary = {
        "Total Income": round(total_income, 2),
        "Total Expenses": round(total_expenses, 2),
        "Net Savings": round(net_savings, 2),
        "Savings Rate (%)": round(savings_rate, 2),
    }
    summary_df = pd.DataFrame(list(summary.items()), columns=["Metric", "Amount"])

    with pd.ExcelWriter("finance_report.xlsx", engine="openpyxl") as writer:
        summary_df.to_excel(writer, sheet_name="Summary", index=False)

        pivot.to_excel(writer, sheet_name="Pivot Table")
        income_pivot.to_excel(writer, sheet_name="Income by Description")


main()

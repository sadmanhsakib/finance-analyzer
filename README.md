# 💰 Finance Analyzer

A Python-based personal finance analysis tool built as a **learning project** to practice and explore the [pandas](https://pandas.pydata.org/) library. It generates realistic synthetic financial transaction data, cleans and processes it, performs meaningful analysis, and exports a polished summary report to Excel.

---

## 📌 Purpose

This project was built to learn and practice core pandas concepts including:

- Reading and writing CSV/Excel files
- Data cleaning (handling missing values, duplicates, inconsistent formatting)
- Filtering and conditional selection
- GroupBy aggregations
- Merging DataFrames
- Pivot tables
- Exporting multi-sheet Excel reports with `openpyxl`

---

## 🧩 Project Structure

```
finance-analyzer/
├── data_generator.py        # Generates synthetic transaction data
├── finance_analyzer.py      # Core analysis and reporting script
├── requirements.txt         # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md
```

> [!NOTE]
> The generated CSV (`transaction.csv`, `cleaned_transactions.csv`) and Excel (`finance_report.xlsx`) files are git-ignored since they are reproducible outputs.

---

## ⚙️ How It Works

### 1. Data Generation — `data_generator.py`

Generates **1,000 synthetic financial transactions** spanning the past year using the `Faker` library. Each transaction includes:

| Column         | Description                                        |
| -------------- | -------------------------------------------------- |
| `date`         | Random date within the last year                   |
| `description`  | Vendor/source name (e.g., "McDonald's", "Salary")  |
| `amount`       | Positive for income, negative for expenses         |
| `category`     | One of 7 categories (see below)                    |
| `account_type` | Debit or Credit (with intentional format variation) |

**Categories:** Food, Transport, Shopping, Utilities, Entertainment, Health, Income

To simulate real-world messy data, the generator intentionally introduces:
- **Inconsistent casing** in `category` (e.g., "Food", "food", "FOOD")
- **Inconsistent formatting** in `account_type` (e.g., "Debit", "  debit", "CREDIT")
- **75 missing values** in `category`
- **100 missing values** in `description`

A fixed random seed (`random.seed(15)`) ensures the dataset is **reproducible** across runs.

### 2. Data Cleaning — `clean_data()`

Applies a standard cleaning pipeline:
- Converts the `date` column to proper `datetime` format
- Strips whitespace and standardizes text columns to **Title Case**
- Fills missing `category` values with `"Unknown"`
- Drops rows where `description` is missing
- Removes duplicate rows

### 3. Filtering — `filter_data()`

Demonstrates pandas filtering operations:
- Extracts the **month** from each transaction date
- Separates transactions into **income** and **expense** DataFrames
- Flags large expenses (absolute amount > $100) with a boolean `is_large` column

### 4. Analysis — `analysis()`

Performs aggregations and generates insights:
- **Spending by category** — total expenses per category, sorted descending
- **Income by month** — total income grouped by month name
- **Expenses by month** — total expenses grouped by month name
- **Monthly summary** — merges income and expense data, calculates **net savings** per month

### 5. Export — `export_data()`

Builds a professional multi-sheet Excel report (`finance_report.xlsx`):

| Sheet                  | Content                                          |
| ---------------------- | ------------------------------------------------ |
| **Summary**            | Total Income, Total Expenses, Net Savings, Savings Rate (%) |
| **Pivot Table**        | Spending broken down by category and month       |
| **Income by Description** | Income broken down by source and month        |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
# Clone the repository
git clone https://github.com/sadmanhsakib/finance-analyzer.git
cd finance-analyzer

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
# Step 1: Generate the synthetic dataset
python data_generator.py
# → Creates transaction.csv

# Step 2: Run the analyzer
python finance_analyzer.py
# → Reads cleaned_transactions.csv and generates finance_report.xlsx
```

---

## 📦 Dependencies

| Package    | Purpose                              |
| ---------- | ------------------------------------ |
| `pandas`   | Data manipulation and analysis       |
| `numpy`    | Numerical operations                 |
| `faker`    | Synthetic data generation            |
| `openpyxl` | Excel file writing                   |

---

## 🧠 Pandas Concepts Practiced

| Concept                | Where Used                                  |
| ---------------------- | ------------------------------------------- |
| `read_csv` / `to_csv`  | Loading and saving CSV data                |
| `to_datetime`          | Date parsing in `clean_data()`, `filter_data()` |
| `str.strip().str.title()` | Text normalization in `clean_data()`    |
| `fillna` / `dropna`   | Handling missing data in `clean_data()`     |
| `drop_duplicates`      | Removing duplicates in `clean_data()`      |
| Boolean indexing       | Filtering income/expenses in `filter_data()` |
| `groupby` + `sum`      | Aggregations in `analysis()`               |
| `merge`                | Combining DataFrames in `analysis()`       |
| `pivot_table`          | Cross-tabulation in `export_data()`        |
| `ExcelWriter`          | Multi-sheet Excel export in `export_data()`|

---

## 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
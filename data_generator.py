from numpy.random import random
import pandas as pd
import random
from faker import Faker

fake = Faker()
# ensures that the same dataset is generated every time
random.seed(42)

categories = [
    "Food",
    "Transport",
    "Shopping",
    "Utilities",
    "Entertainment",
    "Health",
    "Income",
]

descriptions = {
    "Food": ["McDonald's", "KFC", "GrabFood", "FairPrice", "Coffee Bean"],
    "Transport": ["Grab", "Uber", "ComfortDelGro", "Bus Fare", "Petrol"],
    "Shopping": ["Saint Laurent", "Amazon", "Ebay", "IKEA", "Burberry"],
    "Utilities": ["SP Group", "Internet Bill", "M1 Bill", "PUB Bill"],
    "Entertainment": ["Netflix", "Spotify", "Golden Village", "Steam", "Prime"],
    "Health": ["Guardian", "Supplements", "Clinic Visit", "Gym Membership", "Dental"],
    "Income": [
        "Salary",
        "Freelance Payment",
        "Agency Revenue",
        "Dividends",
        "Bonus",
    ],
}


def generate_amount(category):
    if category == "Income":
        return round(random.uniform(2500, 10000), 2)
    # multiplying -1 to get the negative value for deduction
    return round(random.uniform(10, 200) * -1, 2)


rows = []

# generating the dataset
for _ in range(1000):
    category = random.choice(categories)
    rows.append(
        {
            # generates a random date from today to in the last 1 years
            "date": fake.date_between(start_date="-1y", end_date="today").strftime(
                "%Y-%m-%d"
            ),
            "description": random.choice(descriptions[category]),
            "amount": generate_amount(category),
            # writing the category in different cases
            "category": random.choice([category, category.lower(), category.upper()]),
            "account_type": random.choice(["Debit", "Credit", "  debit", "CREDIT"]),
        }
    )

# intentionally making some rows with missing values
for i in random.sample(range(1000), 75):
    rows[i]["category"] = None
for i in random.sample(range(1000), 100):
    rows[i]["description"] = None

# saving the dataset
df = pd.DataFrame(rows)
df.to_csv("transaction.csv", index=False)
print("✅Dataset generated successfully. ")

# 1. In: one expense typed by the user: the date, the category, the amount and how I paid
# 2. Process: check that each answer is ok, ask again if not, then add one line to the file
# 3. Out, file name and columns:
#    expenses.csv, with the columns date;category;amount_eur;payment_method
# 4. Why these columns, and what this file is for:
#    It is my monthly budget tracker. With 200 rows I could see how much I spend per
#    category and per month, find where my money goes, and plan next month's budget.
#    The payment method shows how much cash I use compared to my card.
#
# My two decisions:
# - First time: the file does not exist yet, so I write the header line first.
#   After that I never write it again.
# - Wrong value: I ask again. The amount must be a number above 0, and I accept
#   a comma like 12,50 because that is how we write it in France.

# Your code below
import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"

# Ask the date, Enter means today
date_text = input("Date (YYYY-MM-DD, press Enter for today): ").strip()
if date_text == "":
    date_text = date.today().isoformat()

# Ask the category, it cannot be empty
category = input("Category (rent, food, transport...): ").strip().lower()
while category == "":
    category = input("Category cannot be empty. Category: ").strip().lower()

# Ask the amount until it is a number above 0
amount_text = input("Amount in EUR: ").strip().replace(",", ".")
while True:
    try:
        amount = float(amount_text)
        if amount > 0:
            break
        amount_text = input("The amount must be more than 0. Amount in EUR: ").strip().replace(",", ".")
    except ValueError:
        amount_text = input("Please type a number, like 12.50. Amount in EUR: ").strip().replace(",", ".")

# Ask the amount until it is a number above 0
amount_text = input("Amount in EUR: ").strip().replace(",", ".")
while True:
    try:
        amount = float(amount_text)
        if amount > 0:
            break
        amount_text = input("The amount must be more than 0. Amount in EUR: ").strip().replace(",", ".")
    except ValueError:
        amount_text = input("Please type a number, like 12.50. Amount in EUR: ").strip().replace(",", ".")

# Ask how I paid, only card or cash
payment = input("Payment method (card or cash): ").strip().lower()
while payment not in ["card", "cash"]:
    payment = input("Please type card or cash: ").strip().lower()

# Check if the file is already there, before opening it
file_exists = os.path.exists(FILE_NAME)

# "a" means add at the end, so the old lines stay
with open(FILE_NAME, "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    if not file_exists:
        writer.writerow(["date", "category", "amount_eur", "payment_method"])
    writer.writerow([date_text, category, amount, payment])

print("Saved in", FILE_NAME)

# CHECK IT YOURSELF
# I ran it 3 times: food 12,50 card / rent 650 card / transport 2.15 cash.
# I also typed abc and -5 for the amount, and "bank" for the payment: it asked again.
# expenses.csv has 4 lines: 1 header and 3 expenses. Correct.
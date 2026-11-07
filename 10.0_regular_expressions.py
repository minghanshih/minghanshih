# 1. In: 3 pieces of payment information typed by the user: an IBAN, an invoice number
#    and an amount
# 2. Process: check each one with a pattern. If all 3 are ok, save them. If not, say
#    which ones are wrong.
# 3. Out: "All good" and one new line in payments.csv, or a list of what to fix
# 4. My three fields, and my rules in plain English:
#    IBAN: a French bank account. It starts with FR, then 2 digits, then 23 letters or
#      digits, so 27 characters in total. I remove the spaces and put it in capitals
#      first, because people often type it in groups of 4 like on their bank card.
#      I reject other countries, because my company only pays French accounts.
#    Invoice number: INV, a dash, the year in 4 digits, a dash, 3 digits.
#      Example: INV-2026-041. Small letters "inv" are rejected, because our system
#      always writes it in capitals.
#    Amount: only digits, with no decimals or exactly 2 decimals, with a comma or a dot.
#      4500 and 4500,00 are ok. 12.5 is rejected: in accounting we always write
#      cents with 2 digits. Negative amounts are rejected, a payment is never below 0.

# Your code below
import csv
import os
import re

# My 3 patterns, explained piece by piece:
# IBAN:    FR = the letters F and R
#          \d{2} = exactly 2 digits
#          [A-Z0-9]{23} = exactly 23 characters, each one a capital letter or a digit
IBAN_PATTERN = r"FR\d{2}[A-Z0-9]{23}"
# Invoice: INV- = these 4 characters
#          \d{4} = 4 digits for the year
#          - = a dash
#          \d{3} = 3 digits for the number
INVOICE_PATTERN = r"INV-\d{4}-\d{3}"
# Amount:  \d+ = one digit or more
#          ([.,]\d{2})? = a dot or a comma and 2 digits. The ? means this part is optional
AMOUNT_PATTERN = r"\d+([.,]\d{2})?"


# Remove the spaces and put the IBAN in capitals
def clean_iban(text):
    return text.replace(" ", "").upper()


# True if the whole text follows the pattern, not only a part of it
def is_valid(pattern, text):
    return re.fullmatch(pattern, text) is not None


# My 9 tests: for each field, 1 that must pass and 2 that must fail
tests = [
    ("IBAN", IBAN_PATTERN, clean_iban("FR76 3000 6000 0112 3456 7890 189")),
    ("IBAN", IBAN_PATTERN, clean_iban("DE89 3704 0044 0532 0130 00")),
    ("IBAN", IBAN_PATTERN, clean_iban("FR76 3000 6000")),
    ("Invoice", INVOICE_PATTERN, "INV-2026-041"),
    ("Invoice", INVOICE_PATTERN, "INV-26-41"),
    ("Invoice", INVOICE_PATTERN, "inv-2026-041"),
    ("Amount", AMOUNT_PATTERN, "4500,00"),
    ("Amount", AMOUNT_PATTERN, "12.5"),
    ("Amount", AMOUNT_PATTERN, "-300"),
]
print("--- Tests ---")
for field, pattern, value in tests:
    print(f"{field:<8} {value:<30} {is_valid(pattern, value)}")
print()

# Ask the user for the 3 values
iban = clean_iban(input("IBAN: "))
invoice = input("Invoice number (INV-YYYY-NNN): ").strip()
amount = input("Amount in EUR: ").strip()

# Keep a list of everything that is wrong
errors = []
if not is_valid(IBAN_PATTERN, iban):
    errors.append("IBAN: must start with FR, then 2 digits, then 23 letters or digits.")
if not is_valid(INVOICE_PATTERN, invoice):
    errors.append("Invoice: must look like INV-2026-041.")
if not is_valid(AMOUNT_PATTERN, amount):
    errors.append("Amount: only digits, with 0 or 2 decimals, like 4500 or 4500,00.")

# Save only if the list of errors is empty
if errors:
    print("Not saved. Please fix:")
    for error in errors:
        print(" -", error)
else:
    file_exists = os.path.exists("payments.csv")
    with open("payments.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        if not file_exists:
            writer.writerow(["iban", "invoice_number", "amount_eur"])
        writer.writerow([iban, invoice, amount])
    print("All good, saved in payments.csv")

# CHECK IT YOURSELF
# IBAN:    FR76 3000 6000 0112 3456 7890 189 -> True (ok)
#          DE89 3704 ... (German IBAN) -> False (ok, wrong country)
#          FR76 3000 6000 (too short) -> False (ok)
# Invoice: INV-2026-041 -> True (ok)
#          INV-26-41 -> False (ok, year too short)
#          inv-2026-041 -> False. Small surprise: it looks right to a human,
#          but my rule says capitals only.
# Amount:  4500,00 -> True (ok)
#          12.5 -> False. Borderline: it is a real amount, but I decided cents
#          must have 2 digits.
#          -300 -> False (ok)
# All 9 results are what I expected.
# Note: the tutor refused every question on 7 Nov with "Invalid API Key", so I could not log them.
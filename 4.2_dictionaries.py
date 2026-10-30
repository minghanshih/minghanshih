"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a dictionary describing one customer invoice, written in the code
# 2. Process: read one field, change one, remove one, then show all fields
# 3. Out: the invoice number, then every remaining field with its value
# 4. My object, my five fields, and why those:
#    An invoice we sent to a client (accounts receivable).
#    invoice_number: to find the invoice in the accounting system
#    client: to know who owes the money
#    amount: to know how much we will receive
#    due_date: to know when the payment is expected
#    status: to know if it is paid or not, for cash flow planning

# Your code below
# Describe the invoice with five fields
invoice = {
    "invoice_number": "INV-2026-041",
    "client": "Blue Ocean SAS",
    "amount": 4500,
    "due_date": "2026-11-30",
    "status": "unpaid",
}

# Read one field
print("Invoice number:", invoice["invoice_number"])

# Change one field: the client paid
invoice["status"] = "paid"

# Remove one field: the invoice is paid, so the due date is no longer needed
del invoice["due_date"]

# Show every field with its value
for key, value in invoice.items():
    print(key, ":", value)

# Ask for a field that does not exist, in a safe way
print("payment_method :", invoice.get("payment_method", "not recorded"))

# CHECK IT YOURSELF
# invoice["payment_method"] gave KeyError: 'payment_method' and the program stopped.
# With invoice.get("payment_method", "not recorded") it shows a message instead.

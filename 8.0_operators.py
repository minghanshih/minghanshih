# 1. In: two currency codes, "EUR" and "eur", the same currency typed in two ways
# 2. Process: compare them with == != < > <= >=, then mix the results with and, or, not
# 3. Out: a small table, one line per test, with True or False
# 4. Which two values did I pick, and which result surprised me?
#    I picked "EUR" and "eur". In finance, users type currency codes in many ways,
#    and the program must know they are the same currency.
#    Surprise: "EUR" < "eur" is True. Capital letters come before small letters
#    for Python, so uppercase is "smaller". And "EUR" == "eur" is False, so I need
#    .lower() before comparing.

# Your code below
# My two values
a = "EUR"
b = "eur"

# Every comparison and logical mix, as (text, result) pairs
results = [
    ("a == b", a == b),
    ("a != b", a != b),
    ("a < b", a < b),
    ("a > b", a > b),
    ("a <= b", a <= b),
    ("a >= b", a >= b),
    ("(a == b) and (a < b)", (a == b) and (a < b)),
    ("(a == b) or (a < b)", (a == b) or (a < b)),
    ("not (a == b)", not (a == b)),
    ("a.lower() == b.lower()", a.lower() == b.lower()),
]

# Show the table
print(f"a = {a!r}, b = {b!r}")
print("-" * 36)
for test, result in results:
    print(f"{test:<26} {result}")
# CHECK IT YOURSELF
# Before running I guessed: == False, != True, < False, > True, <= False, >= True,
# and False, or False, not True, lower True.
# I got 6 out of 10 right. I was wrong on <, >, <= and >=, because I thought
# small letters came first.
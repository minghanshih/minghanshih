# 1. In: the number of months the user wants to pay back a 12,000 EUR loan
# 2. Process: turn the text into a whole number, then divide 12,000 by it
# 3. Out: the monthly payment, or a clear message if the answer is wrong
# 4. The two failures, and whether they deserve the same message:
#    - ValueError: the user typed text like "abc" or nothing at all.
#      The problem is the format, so I tell him to type a number like 24.
#    - ZeroDivisionError: the user typed 0. It is a real number, but a loan in 0 months
#      makes no sense, so I explain that he needs at least 1 month.
#    No, they should not have the same message. The user needs to know what to fix.
#
# My limit: 3 attempts. After that I stop asking and tell him to call the bank.
#
# Why catch each error separately: with one big "except", every problem gets the same
# message and the user doesn't know what he did wrong. It can also hide a real bug
# in my code, because Python would catch errors I never planned for.

# Your code below
# The loan and how many tries the user gets
LOAN = 12000
MAX_ATTEMPTS = 3

attempts = 0
while attempts < MAX_ATTEMPTS:
    attempts = attempts + 1
    text = input("In how many months do you want to pay back the loan? ")

    # Try the risky part: turning text into a number, then dividing
    try:
        months = int(text)
        payment = LOAN / months
    # Text or empty line: int() cannot read it
    except ValueError:
        print("This is not a whole number of months. Please type a number like 24.")
    # 0 months: cannot divide by 0
    except ZeroDivisionError:
        print("0 months is not possible: you need at least 1 month to pay back.")
    # No error: show the result and stop asking
    else:
        print(f"You will pay {payment:.2f} EUR per month for {months} months.")
        break
# This part only runs if the loop ended without break, so after 3 wrong answers
else:
    print("3 wrong answers. Please talk to your bank advisor.")

# CHECK IT YOURSELF
# 24: "You will pay 500.00 EUR per month for 24 months." It stops right away.
# 0: "0 months is not possible..." and it asks again.
# abc: "This is not a whole number of months..." and it asks again.
# Empty line: same message as abc, because int("") is also a ValueError.
# 3 wrong answers in a row: "3 wrong answers. Please talk to your bank advisor."
# The program never crashed.
# Note: the tutor refused every question on 7 Nov with "Invalid API Key", so I could not log them.
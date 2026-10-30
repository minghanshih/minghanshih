"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user's answers to a payment confirmation question
# 2. Process: keep asking until the user answers yes or no, with a maximum of 3 attempts
# 3. Out: a summary with the number of attempts, all the answers, and the final result
# 4. My stop condition, my attempt limit, my summary:
#    Stop condition: the answer is "yes" or "no". I accept "Yes", "YES" and " yes "
#    as the same answer, because a user should not lose a payment because of a capital.
#    Limit: 3 attempts. After 3 invalid answers, the payment is cancelled for safety.
#    Summary: attempts used, answers given, and if the payment was confirmed,
#    refused or cancelled.

# Your code below
# Settings and counters
max_attempts = 3
attempts = 0
answers = []
clean = ""

# Keep asking until a valid answer or the limit is reached
while attempts < max_attempts:
    answer = input("Do you confirm the payment of 4500 euros? (yes/no): ")
    attempts = attempts + 1
    answers.append(answer)
    # Remove spaces and capitals so " YES " counts as "yes"
    clean = answer.strip().lower()
    if clean == "yes" or clean == "no":
        break

# Summary of what happened
print("Attempts used:", attempts)
print("Answers given:", answers)
if clean == "yes":
    print("Result: payment confirmed.")
elif clean == "no":
    print("Result: payment refused.")
else:
    print("Result: limit reached, payment cancelled.")

# CHECK IT YOURSELF
# Never the expected answer (maybe, ok, 123): the program stopped after 3 attempts
#   and showed "limit reached, payment cancelled". Correct.
# Answer "  YES  " with capitals and spaces: accepted on the first attempt,
#   "payment confirmed". Correct.

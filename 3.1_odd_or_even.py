"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a number N typed by the user
# 2. Process: go through every number from 1 to N and check if it is odd or even
# 3. Out: one line per number saying "odd" or "even"
# 4. What happens on 0, on a negative number, on a very large number:
#    0: show a message, because there is no number from 1 to 0.
#    Negative: same message, counting from 1 to -4 makes no sense.
#    5000: refuse anything above 100, because nobody reads 5000 lines.

# Your code below
# Ask for a number and turn it into an integer
n = int(input("Type a number: "))

# Check the edge cases before the loop
if n < 1:
    print("Please type a number of 1 or more.")
elif n > 100:
    print("That is too many lines. Please type 100 or less.")
else:
    # Go through every number from 1 to n
    for i in range(1, n + 1):
        # % 2 gives the remainder: 0 means even
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")

# CHECK IT YOURSELF
# 6: 1, 3, 5 are odd and 2, 4, 6 are even, so three odd and three even. Correct.
# 0: shows "Please type a number of 1 or more." As decided.
# -4: shows the same message. As decided.
# 5000: shows "That is too many lines." As decided.

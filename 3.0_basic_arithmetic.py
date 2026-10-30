"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two numbers typed by the user
# 2. Process: turn them into numbers, then add, subtract, multiply and divide
# 3. Out: the four results
# 4. What happens when the second number is zero, and why:
#    I show a message instead of the division result. The other three operations
#    still work, so the user still gets useful answers.

# Your code below
# Ask for two numbers and turn the text into numbers
a = int(input("First number: "))
b = int(input("Second number: "))

# Add, subtract and multiply
print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)

# Divide only if the second number is not zero
if b == 0:
    print("Cannot divide by zero")
else:
    print(a, "/", b, "=", a / b)

# CHECK IT YOURSELF
# 7 and 2: 7 / 2 = 3.5, which is correct. If I used // instead of /, Python would
#   show 3, because // keeps only the whole number and drops the .5.
# 7 and 0: the first three results are shown, then "Cannot divide by zero".

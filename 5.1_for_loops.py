"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the list of 8 monthly closing prices from exercise 4.0
# 2. Process: for each month, compare the price with the average price
# 3. Out: one line per month with the month number, the price, and how far it is
#    above or below the average
# 4. What I compute for each item, and why it is worth showing:
#    The gap between each month's price and the average (105.5 euros).
#    The reader sees at a glance which months were expensive or cheap to buy the stock.

# Your code below
# The same list as in 4.0
prices = [100, 96, 110, 104, 92, 120, 114, 108]

# The average, used to compare each month
average = sum(prices) / len(prices)

# For each month, show its number, its price and its gap with the average
for month, price in enumerate(prices, start=1):
    difference = price - average
    # Decide if the price is above or below the average
    if difference > 0:
        position = "above"
    else:
        position = "below"
    print(f"Month {month}: {price} euros, {abs(difference)} {position} the average")

# CHECK IT YOURSELF
# The program printed 8 lines, and my list has 8 items. No off-by-one.
# enumerate(start=1) makes the months start at 1 instead of 0.

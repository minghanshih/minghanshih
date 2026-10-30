"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of 8 monthly closing prices of a stock (in euros), written in the code
# 2. Process: pick one month, sort the list, compute the average, highest and lowest price
# 3. Out: the whole list, one month, the sorted list, the average, highest, lowest and range
# 4. What my list is about, and what I computed from it:
#    Monthly closing price of a stock, January to August.
#    I computed the average price and the gap between the highest and lowest price.
#    That gap shows how much the price moved: a simple way to see the risk of the stock.

# Your code below
# Monthly closing prices in euros, January to August
prices = [100, 96, 110, 104, 92, 120, 114, 108]

# Show the whole list
print("All prices:", prices)

# Show one item: March is position 2, because Python starts counting at 0
print("March price:", prices[2])

# Show the list sorted from lowest to highest
print("Sorted:", sorted(prices))

# Compute the average, highest, lowest and the gap between them
average = sum(prices) / len(prices)
print("Average price:", average)
print("Highest:", max(prices))
print("Lowest:", min(prices))
print("Range:", max(prices) - min(prices))

# Check on the first three months only
print("Average of first three months:", sum(prices[:3]) / 3)

# CHECK IT YOURSELF
# By hand: (100 + 96 + 110) / 3 = 306 / 3 = 102. The program also shows 102.0. Correct.
# Full average by hand: 844 / 8 = 105.5. Highest 120, lowest 92, range 28. The program agrees.

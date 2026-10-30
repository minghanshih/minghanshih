"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the same list of 8 monthly closing prices as in 4.0
# 2. Process: show it in four different orders without damaging the original
# 3. Out: four reordered lists, then the original list to prove it did not change
# 4. My four orders, and which ones modify the original:
#    1. Low to high with sorted(): returns a new list, original safe
#    2. High to low with sorted(reverse=True): returns a new list, original safe
#    3. Last month first with .reverse(): this CHANGES the list it is used on,
#       so I used it on a copy, not on the original
#    4. Sorted as text with sorted(key=str): new list. Shows how prices imported
#       as text from a file sort wrongly (92 ends up after 120)
#    .sort() and .reverse() modify in place. sorted() and slicing make a copy.

# Your code below
# The same list as in 4.0
prices = [100, 96, 110, 104, 92, 120, 114, 108]

# Order 1: lowest to highest, a new list
print("Low to high:", sorted(prices))

# Order 2: highest to lowest, a new list
print("High to low:", sorted(prices, reverse=True))

# Order 3: last month first. .reverse() changes the list, so I use a copy
prices_copy = prices.copy()
prices_copy.reverse()
print("Last month first:", prices_copy)

# Order 4: sorted as text, a new list
print("Sorted as text:", sorted(prices, key=str))

# Prove the original list was not damaged
print("Original:", prices)

# CHECK IT YOURSELF
# Original printed: [100, 96, 110, 104, 92, 120, 114, 108]
# Same as in 4.0, item by item. The original survived.


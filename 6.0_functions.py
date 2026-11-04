# 1. In: a list of monthly stock prices
# 2. Process: add all the prices and divide by how many months there are
# 3. Out: the average price, as a number
# 4. My function name, and why return rather than print:
#    average_price. You can guess what it does just from the name.
#    I use return because I want to keep the number and use it again, for example to
#    compare it with today's price. With print the number only shows on the screen
#    and I cannot do anything else with it.



# Your code 
# My stock prices from 4.0, January to August
prices = [100, 96, 110, 104, 92, 120, 114, 108]


# Give back the average price of a list of prices
def average_price(prices):
    # An empty list has no average, so I give back 0 instead of crashing
    if len(prices) == 0:
        return 0
    return sum(prices) / len(prices)


# Call it 3 times: the whole period, the first 3 months, the last 3 months
print("Average of all 8 months:", average_price(prices))
print("Average of the first 3 months:", average_price(prices[:3]))
print("Average of the last 3 months:", average_price(prices[-3:]))

# Test with an empty list
print("Average of an empty list:", average_price([]))

# CHECK IT YOURSELF
# Without the if, an empty list gave ZeroDivisionError, because you cannot divide by 0.
# I don't think that is ok, the program should not crash. So now it returns 0.
# The price went up: 102 at the start, 114 at the end.
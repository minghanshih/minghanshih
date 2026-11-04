# 1. In: my list of monthly stock prices from 4.0
# 2. Process, function by function:
#    average_price: gives the average of all the prices
#    latest_price: gives the last price in the list
#    percent_difference: says how many % one price is above or below another
#    latest_vs_average: uses the 3 functions above to answer my question
# 3. Out: one number in %, rounded to 2 decimals
# 4. The question my fourth function answers:
#    Is the stock more expensive or cheaper than usual right now, and by how much?
#    Splitting it in 3 makes it easier to check, because I can test each small part
#    alone. If the final answer is wrong, I know which part to look at.

#Your code below
# My stock prices from 4.0, January to August
prices = [100, 96, 110, 104, 92, 120, 114, 108]


# Give back the average of the prices
def average_price(prices):
    return sum(prices) / len(prices)


# Give back the last price in the list, the most recent month
def latest_price(prices):
    return prices[-1]


# Give back how many % the price is above (+) or below (-) the reference
def percent_difference(price, reference):
    return round((price - reference) / reference * 100, 2)


# Answer my question by using the 3 small functions
def latest_vs_average(prices):
    average = average_price(prices)
    latest = latest_price(prices)
    return percent_difference(latest, average)


# Test each small function alone first
print(average_price([100, 96, 110]))
print(latest_price([100, 96, 110]))
print(percent_difference(110, 100))

# Then the final answer
print("Latest price vs average:", latest_vs_average(prices), "%")

# CHECK IT YOURSELF
# average_price([100, 96, 110]) -> expected 102.0, I got 102.0
# latest_price([100, 96, 110]) -> expected 110, I got 110
# percent_difference(110, 100) -> expected 10.0, I got 10.0
# Final answer: the August price (108) is 2.37% above the average (105.5).
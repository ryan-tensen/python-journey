# Best Time to Buy and Sell Stock
#
# Given an array where nums[i] is the price of a stock on day i.
# Find the maximum profit you can make by buying on one day
# and selling on a later day.
#
# You can only buy once and sell once.
#
# Example:
# prices = [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price=1), sell on day 5 (price=6)
# Profit = 6-1 = 5
#
# prices = [7, 6, 4, 3, 1]
# Output: 0
# Explanation: Prices keep falling, no profit possible


prices = [7, 1, 5, 3, 6, 4]


def max_stock_return(stocks):
    min_price = stocks[0]
    max_profit = 0
    for idx, i in enumerate(stocks):
        if i < min_price:
            min_price = i
        profit = i - min_price
        max_profit = max(max_profit, profit)
    return max_profit


print(max_stock_return(prices))
print(max_stock_return([7, 1, 5, 3, 6, 4]))
print(max_stock_return([7, 6, 4, 3, 1]))
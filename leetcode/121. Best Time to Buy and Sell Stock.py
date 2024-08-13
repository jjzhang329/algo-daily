#if current number is min_price, then just calculate the diff to update max_profit
#if there are numbers smaller than curren_price
#record min_price again and calculate profit


def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
        
    return max_profit
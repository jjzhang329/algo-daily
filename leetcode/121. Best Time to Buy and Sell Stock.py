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

# using 2d dp
# dp[i][0] => 在i天持有股票的最大值
# dp[i][1] => 在i天不持有股票的最大值
# 持有和不持有不等于是买进卖出
# dp[i-1][0] => 从前一天就开始持有
# - prices[i] => 从今天买入开始持有(第一次买入)
# dp[i][0] = max(dp[i-1][0], dp[i-1][0]-prices[i])
# dp[i][1] = max(dp[i-1][1]， dp[i-1][0]+prices[i])
# 最后最大值一定是不持有状态下的最大值


def maxProfit(prices):
    dp = [[0]* 2] * len(prices)
    dp[0][0] = -prices[0]

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i-1][0], dp[i-1][0]-prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
    
    return dp[-1][1]


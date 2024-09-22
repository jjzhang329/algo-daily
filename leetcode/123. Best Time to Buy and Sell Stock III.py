# dp[i][0] => 不操作
# dp[i][1] => 第一次持有
# dp[i][2] => 第一次不持有
# dp[i][3] => 第二次持有
# dp[i][4] => 第二次不持有
# dp[i][0] => dp[i-1][0] => 0
# dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
# dp[i][2] = max(dp[i-1][2], dp[i-1][1]+prices[i])
# dp[i][3] = max(dp[i-1][3], dp[i-1][2]-prices[i])
# dp[i][4] = max(dp[i-1][4], dp[i-1][3]+prices[i])
def max_profit(prices):
    dp = [[0]*4]*len(prices)
    dp[0][1] = -prices[0]
    dp[0][3] = -prices[0]

    for i in range(1, len(prices)):
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        dp[i][2] = max(dp[i-1][2], dp[i-1][1]+prices[i])
        dp[i][3] = max(dp[i-1][3], dp[i-1][2]-prices[i])
        dp[i][4] = max(dp[i-1][4], dp[i-1][3]+prices[i])
    
    return dp[-1][4]

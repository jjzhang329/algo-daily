# 和121的区别是现在可以交易股票多次
# 所以如果今天买入持有股票的话需要从前面不持有股票时推出

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [ [0] * 2 ]*len(prices)
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        
        return dp[-1][1]
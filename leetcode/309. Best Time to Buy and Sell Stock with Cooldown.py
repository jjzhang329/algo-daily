class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 分析不同的几种状态
            # 0 持有
            # 1 非持有
            # 2 今日卖出,前一天必定是持有状态
            # 3 冷冻， 前一天必定是状态2，在前一天卖出

        # 1. 持有状态
            # 从前一天开始持有 [i-1][0]
            # 今天买入持有，那么前一天是非持有[i-1][1]-prices[i]
            # 或者前一天是冷冻期 [i-1][3]-prices[i]
        # 2. 非持有状态
            # 前一天延续 [i-1][1]
            # 前一天是冷冻期 [i-1][3]
        # 3. 今日卖出 [i-1][0] + prices[i]
        # 4. 冷冻状态， [i-1][2]
        dp = [ [0] * 4 for _ in range(len(prices))]
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i], dp[i-1][3]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][3])
            dp[i][2] = dp[i-1][0] + prices[i]
            dp[i][3] = dp[i-1][2]
        
        return max(dp[-1][0], dp[-1][1], dp[-1][2], dp[-1][3])
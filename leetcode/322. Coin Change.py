# 完全背包问题
# 求最小的硬币个数
# dp[j] => 装满目标为j的背包最少需要几个硬币
# 不装当前硬币时，最少需要dp[j-coin]个硬币
# 所以放入当前硬币就需要 + 1
# dp[j] = min(dp[j], dp[j-coin]+1)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount+1):
                if dp[j-coin] != float('inf'):
                    dp[j] = min(dp[j], dp[j-coin]+1)
        
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
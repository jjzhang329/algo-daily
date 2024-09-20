# 01背包问题
# 如果将nums拆为正负两组
# 只要能满足一组target数字，那就可以得到target
# j = (sum + target) // 2
# 如果不能整除，return 0, 代表无法达到target
# dp[j] += dp[j-num] => 装满容量j的背包有几种方法


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        size = (sum(nums) + target) // 2

        if (sum(nums) + target) % 2 != 0 or size < 0:
            return 0
        
        dp = [0] * (size + 1)
        dp[0] = 1

        for num in nums:
            for j in range(size, num-1, -1):
                dp[j] += dp[j-num]
        
        return dp[size]
# 题目要求将nums拆分成两个总和相等的subset
# 每个subset_sum = sum(nums) // 2
# 同理，如果总和是奇数，那么直接return False,因为没办法拆成两半
# 可以把target = sum(nums) // 2 看成最大背包容量
# 然后看能不能把背包装满 target == dp[target]
# 1. dp[j] => 背包容量为j的最大值
# 2. dp[target] = max(dp[j], dp[j-weight] + value)， weight == value
# 3. 初始化为0，因为value不能为负
# 4. j 需要从后向前遍历，来避免重复加入背包
# 5. dp[target] 就是当背包容量为target时，最大subset
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [0] * (target + 1)

        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = max(dp[j], dp[j-num]+num)

        return dp[target] == target
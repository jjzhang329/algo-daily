# 1. dp[i] => 有i个节点的bst
# 2. 因为是bst,左边节点小于当前j,右边节点大于j
# 比如 i = 3, j = 2, 那么左边有j-1 = 1个节点，右边是i-j = 1个节点
# 整体排列应该是 左边排列 * 右边排列
# 递推公式： dp[i] += dp[j-1] + dp[i-j]
# 3. 初始 dp[0] = 1， 当节点为空时，也是1种排列方式
# 4. 从左到右按顺序遍历
# 5. print dp

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1] * dp[i-j]

        return dp[n]
        
# 746. Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        #因为跳到下一步才产生cost,所以第一步在index0或者index1的时候没有任何cost

        for i in range(2, len(cost)+1):
            step_1 = dp[i-1] + cost[i-1]
            step_2 = dp[i-2] + cost[i-2]
            dp[i] = min(step_1, step_2)
        
        return dp[-1]
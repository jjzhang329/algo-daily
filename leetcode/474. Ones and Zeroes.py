# Example 1:
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

# 依然是01背包
# 但是此时背包容量是2维的 dp[i][j] => dp[m][n]
# 每个单独的str中的1和0的数量就是物品重量
# 套用 01 背包公式 dp[j] = max(dp[j], dp[j-weight]+value)
# 此时weight => (x, y) => (i-x, j-y)
# value = 1, 代表可以把当前str加入背包中，数量+1

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [ [0] * (n+1) for _ in range(m+1) ]

        def counting(str):
            result = [0, 0] #m, n
            for s in str:
                if s == '1':
                    result[1] += 1
                elif s == '0':
                    result[0] += 1
            
            return tuple(result)

        weights = list(map(counting, strs))
        
        for x, y in weights:
            if x > m or y > n:
                continue

            for i in range(m, x-1, -1):
                for j in range(n, y-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-x][j-y]+1)
        
        return dp[m][n]

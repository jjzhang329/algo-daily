# dp[i][j] => 以i为结尾的s,以j为结尾的t相同的subsequence的个数
# 注意此题不是求最大长度而是求个数
# s[i-1] == t[j-1]时：下面两种情况相加
    # 不使用s[i-1], dp[i-1][j],因为可能之前已经有matched s[i]
    # dp[i-1][j-1]， 延续上一个相同的状态
# else 不相等，那不能用s[i-1] dp[i][j] = dp[i-1][j]
# 

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sizet = len(t)+1
        sizes = len(s)+1

        dp = [ [0]*sizet for _ in range(sizes) ]

        for i in range(sizes):
            dp[i][0] = 1
        
        for i in range(1, sizes):
            end = i+1 if i < len(t) else sizet
            for j in range(1, end):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]       
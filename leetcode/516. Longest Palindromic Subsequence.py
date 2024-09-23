# dp[i][j] => 在区间s[i:j]的中间最长的palindrome
# if s[i] == s[j]:
#   也就是说可以从前面的最长palindrom + 2 => dp[i+1][j-1] + 2
# else: 可以选择s[i:j-1]或者s[i+1:j]
# 遍历顺序，i是倒序，j是从左往右

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [ [0]* len(s) for _ in range(len(s)) ]

        for i in range(len(s)):
            dp[i][i] = 1
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
        return dp[0][-1]
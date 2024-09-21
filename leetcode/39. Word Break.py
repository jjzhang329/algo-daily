class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [False] * (size+1)
        dp[0] = True
    
        for j in range(1, size+1):
            for word in wordDict:
                if j >= len(word):
                    dp[j] = dp[j] or (dp[j-len(word)] and word == s[j-len(word): j])
        
        return dp[size]
    
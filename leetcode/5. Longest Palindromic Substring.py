class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''

        for i in range(len(s)):
            odd_len= self.palindrome(s, i, i)
            if odd_len > len(longest):
                dist = odd_len // 2
                longest =s[i-dist:i+dist+1]

            even_length = self.palindrome(s, i, i+1)
            if even_length > len(longest):
                dist = ( even_length // 2 ) - 1
                longest = s[i-dist:i+1+dist+1]

        return longest


            

    def palindrome(self, s, left, right):
        while left >= 0 and left < len(s) and right >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
           
        return right - left - 1
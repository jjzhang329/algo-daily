# find the window that has all chars in t
# then start shriking the window until window not valid anymore


from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ''

        countT = Counter(t)
        required = len(countT)
        left, right = 0, 0 
        size = 0 
        window = defaultdict(int)
        result = float('inf'), None, None

        while right < len(s):
            char = s[right]
            window[char] += 1

            if char in countT and window[char] == countT[char]:
                size += 1
            
            while left <= right and size == required:
                char = s[left]
                if right - left + 1 < result[0]:
                    result = right - left + 1, left, right
                
                window[char] -= 1
                
                if char in countT and window[char] < countT[char]:
                    size -= 1
                
                left += 1
            
            right += 1
        
        return '' if result[0] == float('inf') else s[result[1]:result[2]+1]
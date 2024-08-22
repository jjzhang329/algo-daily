# using sliding window
# dont need to shrink window, just check if able to extend window
# use a freq hashmap
# valid = window_size - max_frequency <= k
# if valid, extend window, else, move start point to next 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0 
        freq = {}
        max_freq = 0 
        longest = 0 

        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            max_freq = max(max_freq, freq[s[end]])

            is_valid = (end - start + 1 - max_freq <= k)
            if not is_valid:
                freq[s[start]] -= 1
                start += 1
            
            longest = end - start + 1
        
        return longest
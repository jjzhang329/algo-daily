# get the frequency of characters in s1
# using a sliding window of size of len(s1)
# use a frequency mapping for s2, everytime we move the window
# decrement the previous char, and increment the next char
# if we can find a match of frequency of characters in the window
# we find a permutation
# if not, we need to slide the window to the right and update the frequency mappings

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        for i in range(len(s2)-len(s1)):
            if self.matches(s1Count, s2Count):
                return True
            s2Count[ord(s2[i+len(s1)]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] -= 1

        return self.matches(s1Count, s2Count)

    def matches(self, s1, s2):
        for i in range(26):
            if s1[i] != s2[i]:
                return False
        
        return True
    
# optimized solution, instead of comparing s1mapping and s2mapping each time, 
# we can keep recording a matcher, if matcher == 26, it means frequencies all matched
# everytime we slide the window we need to update the matcher


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matcher = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matcher += 1
        
        for i in range(len(s2)-len(s1)):
            if matcher == 26:
                return True
            left = ord(s2[i]) - ord('a')
            right = ord(s2[i+len(s1)]) - ord('a')

            s2Count[right] += 1
            if s2Count[right] == s1Count[right]:
                matcher += 1
            elif s2Count[right] == s1Count[right] + 1:
                matcher -= 1

            s2Count[left] -= 1
            if s2Count[left] == s1Count[left]:
                matcher += 1
            elif s2Count[left] == s1Count[left] - 1:
                matcher -= 1

        return matcher == 26

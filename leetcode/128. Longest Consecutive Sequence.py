# use a set to save all numbers
# check in num + 1 in set to record streak
# start counting from  num - 1 not in set, 
# because we want to start couting from smallest number in a sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num 
                current = 1
            
                while current_num + 1 in num_set:
                    current_num += 1
                    current += 1 
                
                longest = max(current, longest)

        return longest
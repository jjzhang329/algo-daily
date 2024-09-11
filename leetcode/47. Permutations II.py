# 排序问题， 需要用used来判断如何取下一个数字
# 树层去重，需要看used[i-1]判断，需要sort nums
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.backtracking(nums, result, [], [False] * len(nums))
        return result 
    
    def backtracking(self, nums, result, path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i-1] == nums[i] and used[i-1] == False):
                continue
            
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, result, path, used)
            used[i] = False 
            path.pop()
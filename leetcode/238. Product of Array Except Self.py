# O(N),记录prefix product和suffix product
# 优化： space O(1),用一个array记录，用一个variable记录变量suffix

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]
        
        return result
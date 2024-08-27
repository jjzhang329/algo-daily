# using the mid point to start bsearch
# if the array is not rotated or rotated n times
# last element must be greater than first element
# otherwise, if nums[mid] > nums[0], search right
# else, search left 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        if len(nums) == 1 or nums[0] < nums[right]:
            return nums[0]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                left = mid+1
            else:
                right = mid - 1
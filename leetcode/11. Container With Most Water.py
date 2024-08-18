# two pointer, always use the higher bar

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result= 0 
        left, right = 0, len(height)-1

        while left < right:
            width = right - left 
            area  = min(height[right], height[left]) * width
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

            result = max(result, area)

        return result

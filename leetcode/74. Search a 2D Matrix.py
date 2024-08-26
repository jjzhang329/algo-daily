class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_size = len(matrix)
        col_size = len(matrix[0])

        r = 0 
        while r < row_size:
            if target >= matrix[r][0] and target <= matrix[r][col_size-1]:
                if self.bsearch(matrix[r], target):
                    return True
            
            r += 1

        return False 
        
    def bsearch(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
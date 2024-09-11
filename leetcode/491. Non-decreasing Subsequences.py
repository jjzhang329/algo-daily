# 排序问题
# 不能用startIdx来选数字，需要用set记录每一层用过的num

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, 0, [], result)
        return result 

    def backtracking(self, nums, idx, path, result):
        if len(path) > 1:
            result.append(path[:])

        used = set()

        for i in range(idx, len(nums)):
            if nums[i] in used or (path and nums[i] < path[-1]):
                continue

            used.add(nums[i])
            path.append(nums[i])
            self.backtracking(nums, i+1, path, result)
            path.pop()
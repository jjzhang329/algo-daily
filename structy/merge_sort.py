from collections import deque

def merge_sort(nums):
  pass # todo
  if len(nums) <= 1:
    return nums
  mid = len(nums) // 2
  left = merge_sort(nums[:mid])
  right = merge_sort(nums[mid:])

  return merge(left, right)

def merge(left, right):
  result = []
  left = deque(left)
  right = deque(right)
  while left and right:
    if left[0] < right[0]:
      result.append(left.popleft())
    else:
      result.append(right.popleft())
  result += left 
  result += right
  return result
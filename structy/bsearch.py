def binary_search(numbers, target):
  pass # todo
  left, right = 0, len(numbers)-1

  while left <= right:
    mid =  left + (right-left) // 2
    if numbers[mid] == target:
      return  mid
    elif numbers[mid] < target:
      left = mid + 1
    else:
      right = mid -1

  return -1
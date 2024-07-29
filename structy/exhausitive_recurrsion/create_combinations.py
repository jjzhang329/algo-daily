def create_combinations(items, k):
  pass # todo
  if k == 0:
    return [[]]
    
  if k > len(items):
    return []

  first = items[0]
  combs = create_combinations(items[1:], k-1)
  combos_with_first = []
  for comb in combs:
    combos_with_first.append([first, *comb])

  combos_without_first = create_combinations(items[1:], k)

  return combos_with_first + combos_without_first

# n = length of items
# k = target length
# Time: ~O(n choose k)
# Space: ~O(n choose k)
#binomial coefficient

def permutations(items):
  if not items:
    return [[]]
  
  first = items[0]
  remaining = items[1:]
  perms = permutations(remaining)
  result = []
  for perm in perms:
    for i in range(len(perm) + 1):
      result.append([*perm[:i], first, *perm[i:]])
    
  return result
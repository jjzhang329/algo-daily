def quickest_concat(s, words):
  result = _quickest_concat(s, words, {})
  if result == float('inf'):
    return -1

  return result

def _quickest_concat(s, words, memo):
  pass # todo
  if s in memo:
    return memo[s]
  if len(s) == 0:
    return 0
  minimum = float('inf')
  
  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      count = 1 + _quickest_concat(suffix, words, memo)
      minimum = min(count, minimum)
  memo[s] = minimum 
  return memo[s]

quickest_concat('caution', ['ca', 'ion', 'caut', 'ut']) # -> 2
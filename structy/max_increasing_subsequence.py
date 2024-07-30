def max_increasing_subseq(numbers):
  pass # todo
  return _max_increasing_subseq(numbers, 0, float('-inf'), {})

def _max_increasing_subseq(numbers, i, prev, memo):
  if i == len(numbers):
    return 0
  key = (i, prev)
  if key in memo:
    return memo[key]
  current = numbers[i]
  options = []
  
  exclude = _max_increasing_subseq(numbers, i+1, prev, memo)
  options.append(exclude)
  if current > prev:
    include = 1 + _max_increasing_subseq(numbers, i+1, current, memo)
    options.append(include)

  memo[key] = max(options)
  return memo[key]
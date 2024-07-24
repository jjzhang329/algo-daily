import math
def summing_squares(n):
  return _summing_squares(n, {})
  
def _summing_squares(n, memo):
  pass # todo
  if n in memo:
    return memo[n]
    
  if n == 0:
    return 0
    
  min_square = float('inf')
  for i in range(1, math.floor(math.sqrt(n)) + 1):
    square = i * i 
    num_squares = 1 + _summing_squares(n - square, memo)
    min_square = min(min_square, num_squares)
  memo[n] = min_square
  return memo[n]
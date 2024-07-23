def tribonacci(n):
  memo = {}
  return _tribonacci(n, memo)
  
def _tribonacci(n, memo):
  pass # todo
  if n <= 1:
    return 0

  if n == 2:
    return 1
  if n in memo:
    return memo[n]
  memo[n] = _tribonacci(n-3, memo) + _tribonacci(n-2, memo) + _tribonacci(n-1,memo)

  return memo[n]

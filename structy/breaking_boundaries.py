# return number of ways from starting position (r, c), that can go out of bound
# 3, 4, 2, 0, 0

# This input asks us to count the numbers of ways
# to move out of bounds in a 3 by 4 grid, starting at
# position (0, 0) if we could take at most 2 moves.

# The answer is 4 because of these 4 distinct ways:
#  1. left
#  2. up
#  3. right, up
#  4. down, left
def breaking_boundaries(m, n, k, r, c):
  return _breaking_boundaries(m, n, k, r, c, {})

def _breaking_boundaries(m, n, k, r, c, memo):
  pass # todo
  row_inbounds = 0 <= r < m 
  col_inbounds = 0 <= c < n
  key = (k, r, c)
  if key in memo:
    return memo[key]
  deltas = [[0,1], [1,0], [0,-1], [-1,0]]
  if not row_inbounds or not col_inbounds:
    return 1 
  if k == 0:
    return 0
  ways = 0
  for delta in deltas:
    row, col = delta
    ways += _breaking_boundaries(m, n, k-1, r+row, c+col,memo)
  memo[key] = ways
  return memo[key]
def count_paths(grid):
  pass # todo  
  return traverse(grid, 0, 0)

def traverse(grid, r, c, memo={}):
  pos = (r, c)
  if pos in memo:
    return memo[pos]
  row_inbound = 0 <= r < len(grid)
  col_inbound = 0 <= c < len(grid[0])

  if not row_inbound or not col_inbound or grid[r][c] == 'X':
    memo[pos] = 0
    return 0

  if r == len(grid) -1 and c == len(grid[0]) -1:
    return 1

  memo[pos] = traverse(grid, r+1, c, memo) + traverse(grid, r, c+1, memo)
  return memo[pos]

grid = [
  ["O", "O", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "X"],
  ["X", "O", "O", "O", "O", "O"],
  ["X", "X", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O"],
]
count_paths(grid) # -> 42
def max_path_sum(grid):
  pass # todo
  return traverse(grid, 0, 0, {})


def traverse(grid, r, c, memo):
  pos = (r, c)
  if pos in memo:
    return memo[pos]
  if r == len(grid) or c == len(grid[0]):
    return float('-inf')
    
  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return grid[r][c]

  down = traverse(grid, r+1, c, memo)
  right = traverse(grid, r, c+1, memo)

  memo[pos] = grid[r][c] + max(down, right)
  return memo[pos]
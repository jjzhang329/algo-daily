def island_count(grid):
  pass # todo
  count = 0
  visited = set()
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if traverse(r, c, grid, visited):
        count += 1

  return count 

def traverse(r, c, grid, visited):
  if not is_inbound(r, c, grid) or (r, c) in visited or grid[r][c] == 'W':
    return False 

  visited.add((r,c))

  traverse(r+1, c, grid, visited)
  traverse(r, c+1, grid, visited)
  traverse(r-1, c, grid, visited)
  traverse(r, c-1, grid, visited)

  return True
  

def is_inbound(r, c, grid):
  if r < 0 or r >= len(grid):
    return False

  if c < 0 or c >= len(grid[0]):
    return False 

  return True


grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

island_count(grid) # -> 4
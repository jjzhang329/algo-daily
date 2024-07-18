def minimum_island(grid):
  pass # todo
  smallest = float('inf')
  visited = set()
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      size = traverse(r, c, grid, visited)
      if size > 0 and size < smallest:
        smallest = size 

  return smallest

def traverse(r, c, grid, visited):
  if not is_inbound(r, c, grid) or (r, c) in visited or grid[r][c] == 'W':
    return 0
  visited.add((r, c))
  size = 1

  size += traverse(r+1, c, grid, visited)
  size += traverse(r, c+1, grid, visited)
  size += traverse(r-1, c, grid, visited)
  size += traverse(r, c-1, grid, visited)

  return size
def is_inbound(r, c, grid):
  if r < 0 or r >= len(grid):
    return False

  if c < 0 or c >= len(grid[0]):
    return False 

  return True



grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

minimum_island(grid) # -> 2
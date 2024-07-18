from collections import deque

def best_bridge(grid):
  pass # todo
  main_island = set()
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      potential_island = dfs(r, c, grid, set())
      if len(potential_island) > 0:
        main_island = potential_island

  print(main_island)

  dq = deque([])
  visited = set(main_island)
  for pos in main_island:
    r, c = pos 
    dq.append((r, c, 0))
  while dq:
    r, c, distance = dq.popleft()
    if grid[r][c] == 'L' and (r, c) not in main_island:
      return distance - 1 

    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for delta in dirs:
      delta_row, delta_col = delta 
      new_row = r + delta_row 
      new_col = c + delta_col 
      row_inbound = 0 <= new_row < len(grid)
      col_inbound = 0 <= new_col < len(grid[0])

      if row_inbound and col_inbound and (new_row, new_col) not in visited:
        visited.add((new_row, new_col))
        dq.append((new_row, new_col, distance+1))
      

def dfs(r, c, grid, visited):
  row_inbound = 0 <= r < len(grid)
  col_inbound = 0 <= c < len(grid[0])
  if not row_inbound or not col_inbound:
    return visited
    
  if (r, c) in visited or grid[r][c] == 'W':
    return visited

  visited.add((r, c))
  dfs(r+1, c, grid, visited)
  dfs(r-1, c, grid, visited)
  dfs(r, c+1, grid, visited)
  dfs(r, c-1, grid, visited)

  return visited

grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]
best_bridge(grid) # -> 1
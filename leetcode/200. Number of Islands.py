class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited= set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited:
                    count += self.dfs(r, c, grid, visited)
        
        return count
    
    def dfs(self, r, c, grid, visited):
        key = (r, c)
        if key in visited:
            return 0
        
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
            return 0

        visited.add(key)

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for row, col in directions:
            self.dfs(r+row, c+col, grid, visited)
        
        return 1
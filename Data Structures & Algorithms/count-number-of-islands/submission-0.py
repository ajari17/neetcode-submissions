class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    self.dfs(grid,row,col)
                    islands += 1
        return islands
    def dfs(self,grid,r,c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        self.dfs(grid,r-1,c)
        self.dfs(grid,r+1,c)
        self.dfs(grid,r,c-1)
        self.dfs(grid,r,c+1)
            
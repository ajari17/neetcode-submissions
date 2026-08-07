class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                maxx = max(maxx,self.dfs(grid,row,col))
        return maxx


    def dfs(self,grid,r,c):
        if r >= len(grid) or r < 0 or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        return (1 + 
        self.dfs(grid,r+1,c)+
        self.dfs(grid,r-1,c)+
        self.dfs(grid,r,c+1)+
        self.dfs(grid,r,c-1))

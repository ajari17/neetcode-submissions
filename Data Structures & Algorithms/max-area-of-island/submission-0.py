class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        areas = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                areas.append(self.dfs(grid,row,col))
        return max(areas)


    def dfs(self,grid,r,c):
        if r >= len(grid) or r < 0 or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        return (1 + 
        self.dfs(grid,r+1,c)+
        self.dfs(grid,r-1,c)+
        self.dfs(grid,r,c+1)+
        self.dfs(grid,r,c-1))

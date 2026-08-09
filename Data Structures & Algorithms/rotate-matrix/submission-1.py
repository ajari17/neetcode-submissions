class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #transpose  
        n = len(matrix)
        for row in range(n):
            for col in range(row+1,n):
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
        #flip
        for row in range(n):
            for col in range(n//2):
                matrix[row][col],matrix[row][n-col-1] = matrix[row][n-col-1],matrix[row][col]
        
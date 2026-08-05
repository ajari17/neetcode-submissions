class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) 
        left, right = 0, len(matrix) - 1
        top, bottom = 0, len(matrix[0]) - 1
        while left < right and top < bottom:
            for i in range(right - left):
                #save top left
                top_left = matrix[top][left+i]
                #Move bottom-left into top-left
                matrix[top][left + i] = matrix[bottom - i][left]
                #Move bottom-right into bottom-left        
                matrix[bottom-i][left] = matrix[bottom][right-i]
                # Move top-right into bottom-right
                matrix[bottom][right-i] = matrix[top + i][right]
                # Move top-left (saved) into top-right
                matrix[top+i][right] = top_left
                
            left += 1
            right -= 1
            top += 1
            bottom -= 1
            

         
        
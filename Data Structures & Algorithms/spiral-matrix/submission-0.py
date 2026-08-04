class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while left <= right and top <= bottom:
            for c in range(left,right+1):# left to right along the TOP border
                res.append(matrix[top][c])
            top += 1
            for c in range(top, bottom+1):# up to down along the RIGHT border
                res.append(matrix[c][right])
            right -= 1
            if top <= bottom:
                for c in range(right, left-1,-1):# right to left along the BOTTOM border
                    res.append(matrix[bottom][c])
                bottom -= 1
            if left <= right:
                for c in range(bottom, top-1,-1):# down to up along the LEFT border
                    res.append(matrix[c][left])
                left += 1

        return res



            
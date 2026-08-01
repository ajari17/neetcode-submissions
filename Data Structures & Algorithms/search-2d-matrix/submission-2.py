class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for b in matrix:
            low = 0
            high = len(b) - 1
            while low <= high:
                mid = (high+low) // 2
                if b[mid] == target:
                    return True
                if b[mid] < target:
                    low = mid + 1
                if b[mid] > target:
                    high = mid - 1
        return False

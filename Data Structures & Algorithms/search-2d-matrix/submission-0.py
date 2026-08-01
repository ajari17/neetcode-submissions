class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for a in matrix:
            for b in a:
                nums.append(b)
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high+low) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                low = mid + 1
            if nums[mid] > target:
                high = mid - 1
        return False
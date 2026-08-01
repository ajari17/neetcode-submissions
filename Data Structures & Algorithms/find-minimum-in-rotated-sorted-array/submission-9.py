class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        lowest = nums[0]
        
        while left <= right:
            # OPTIMIZATION: If the current window is already sorted,
            # nums[left] is the smallest element in this window.
            if nums[left] < nums[right]:
                lowest = min(lowest, nums[left])
                break
                
            mid = (left + right) // 2
            lowest = min(lowest, nums[mid])
            
            # Decide which half to discard
            if nums[mid] >= nums[left]:
                left = mid + 1  # Left half is sorted, min must be on the right
            else:
                right = mid - 1 # Right half is sorted, min must be on the left
                
        return lowest
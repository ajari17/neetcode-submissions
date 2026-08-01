class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        if nums[left] <= nums[right]:
            return nums[left]
        lowest = 1000
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                lowest = min(nums[left], lowest)
                left = mid + 1
            elif nums[right] >= nums[mid]:
                lowest = min(nums[mid], lowest)
                right = mid - 1
            

        return lowest
        

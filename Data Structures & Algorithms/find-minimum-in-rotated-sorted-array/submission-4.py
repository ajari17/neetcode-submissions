class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        if nums[left] <= nums[right]:
            return nums[left]
        lowest = 1000
        cur_low = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                cur_low = nums[left]
                left = mid + 1
            elif nums[right] >= nums[mid]:
                cur_low = nums[mid]
                right = mid - 1
            lowest = min(cur_low, lowest)

        return lowest
        

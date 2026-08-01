class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        lowest = 1000
        while l <= r:
            mid = (l+r) // 2
            if nums[l] <= nums[mid]:
                lowest = min(lowest,nums[l])
                l = mid + 1
            if nums[r] >= nums[mid]:
                lowest = min(lowest,nums[mid])
                r = mid - 1
        return lowest
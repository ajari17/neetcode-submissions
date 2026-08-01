class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = 0
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                if nums[mid] > target:
                    right = mid - 1
        else:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[left] <= nums[mid]:#left sorted
                    if nums[left] <= target <= nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                if nums[right] >= nums[mid]:
                    if nums[mid] <= target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
    
        return -1
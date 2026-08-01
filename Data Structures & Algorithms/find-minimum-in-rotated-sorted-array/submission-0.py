class Solution:
    def findMin(self, nums: List[int]) -> int:
        while nums[0] > nums[len(nums) - 1]:
            temp = nums[len(nums) - 1]
            nums.insert(0,temp)
            nums.pop(len(nums) - 1)
       # print(nums)
        return nums[0]
        
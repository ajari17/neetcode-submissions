class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        cur_max = nums[0]
        for n in nums[1:]:
            cur_max = max(n, cur_max + n)
            maxx = max(cur_max, maxx)
        return maxx
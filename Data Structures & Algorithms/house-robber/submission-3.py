from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        sums = []
        @cache
        def dfs(cur_sum, i):
            if i >= len(nums):
                sums.append(cur_sum)
                return 
            else:#we do rob the house
                dfs(cur_sum,i+1)
                cur_sum += nums[i]
                dfs(cur_sum,i+2)
        dfs(0,0)
        return max(sums)
        
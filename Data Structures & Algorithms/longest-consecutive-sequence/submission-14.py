class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        arr = set(nums)
        for num in nums:
            if num-1 not in arr:
                cur = 0
                while (num+cur) in arr:
                    cur += 1
                longest = max(cur, longest)
        return longest

        
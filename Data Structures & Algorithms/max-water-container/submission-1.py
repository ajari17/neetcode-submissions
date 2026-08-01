class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxx = float("-inf")
        while l < r:
            cur_max = min(heights[r],heights[l]) * (r-l)
            maxx = max(cur_max, maxx)
            if heights[r] < heights[l]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
                l += 1
        return maxx
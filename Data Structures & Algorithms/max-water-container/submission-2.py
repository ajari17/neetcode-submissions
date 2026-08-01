class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxx = -999
        while i < j:
            area = min(heights[i],heights[j]) * (j - i)
            maxx = max(area, maxx)
            if heights[i] < heights[j]: i += 1
            elif heights[j] < heights[i]: j -= 1
            else:
                i+=1
                j-=1
        return maxx
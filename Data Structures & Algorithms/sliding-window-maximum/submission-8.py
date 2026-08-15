class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        nums = [-x for x in nums]
        heap = []
        for i in range(k):
            heap.append((nums[i],i))
        heapq.heapify(heap)

        l, r = 0, k
        res = [-heap[0][0]]
        for r in range(k,len(nums)):
            heapq.heappush(heap,(nums[r],r))
            l = r-k+1
            while heap[0][1] < l:
                heapq.heappop(heap)
            res.append(-heap[0][0])

        return res
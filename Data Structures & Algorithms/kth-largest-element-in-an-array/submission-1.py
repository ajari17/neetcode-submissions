class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = nums
        heapq.heapify_max(max_heap)
        largest = 0
        for _ in range(k):
            largest = heapq.heappop_max(max_heap)
        return largest

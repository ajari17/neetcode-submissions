class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush_max(max_heap,(dist,[x,y]))
            while len(max_heap) > k:
                heapq.heappop_max(max_heap)
        res = []
        for dist,point in max_heap:
            res.append(point)
        return res
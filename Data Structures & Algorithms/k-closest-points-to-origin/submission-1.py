class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        fin = []
        resfinal = []
        heapq.heapify(res)
        for point in points:
            x = point[0]
            y = point[1]
            #points: x,y and 0,0
            dist = math.sqrt((x**2)+(y**2))
            heapq.heappush(res,dist)
        heapq.heapify(res)
        for _ in range(k):
            fin.append(heapq.heappop(res))
            heapq.heapify(res)
        for point in points:
            x = point[0]
            y = point[1]
            dist = math.sqrt((x**2)+(y**2))
            if dist in fin:
                resfinal.append(point)
        return resfinal
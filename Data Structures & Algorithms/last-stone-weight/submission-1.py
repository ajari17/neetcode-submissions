class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(x,y)
            if x != y:
                y = x-y
                heapq.heappush(stones,y)
        return -stones[0] if stones else 0
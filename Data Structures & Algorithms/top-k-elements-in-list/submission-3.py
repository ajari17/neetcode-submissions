class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = list(Counter(nums).values())
        freqs = [-x for x in freqs]
        heapq.heapify(freqs)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs))
        res = [-x for x in res]
        freqs = Counter(nums)
        fin = []
        for key,val in freqs.items():
            if freqs[key] in res:
                fin.append(key)
        return fin
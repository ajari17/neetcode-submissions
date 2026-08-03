class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def steps(n):
            if n in cache:
                return cache[n]
            if n < 0:
                return 0 
            if n == 0:
                return 1
            cache[n] = steps(n-1) + steps(n-2)
            return cache[n]
        return steps(n)

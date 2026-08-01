class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Initialize an empty list
        pairs = []

        # 2. Loop through the paired elements
        for p, s in zip(position, speed):
            # 3. Append each pair as a new list
            pairs.append([p, s])

        stack = []
        for p,s in sorted(pairs)[::-1]:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack) 

        
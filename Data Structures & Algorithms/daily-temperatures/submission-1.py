class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []#REMEMBER ITS (temp,index)
        res = [0] * len(temperatures)
        for i in range((len(temperatures))):
            while stack and stack[-1][0] < temperatures[i]:
                resIndex = stack[-1][1]
                stack.pop()
                res[resIndex] = (i - resIndex)
            stack.append((temperatures[i],i))
        return res

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*(len(temperatures))
        stack = []#(temp,index)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                ans[stackIndex] = (i - stackIndex)
            stack.append((temperatures[i],i))
            
        return ans

        
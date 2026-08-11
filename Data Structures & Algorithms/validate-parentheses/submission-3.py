class Solution:
    def isValid(self, s: str) -> bool:
        par = {")":"(","]":"[","}":"{"}
        stack = []
        for char in s:
            if char in par:
                if stack and par[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack: return False
        return True
        
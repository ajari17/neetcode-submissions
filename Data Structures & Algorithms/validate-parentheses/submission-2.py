class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {"]":"[","}":"{",")":"("} 
        for char in s:
            if char in mapp:
                if len(stack) != 0 and stack[-1] == mapp[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False  
        
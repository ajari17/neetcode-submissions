class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(["+","-","*","/"])
        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                else:
                    stack.append(a/b)
        return int(stack[-1])
                    
        
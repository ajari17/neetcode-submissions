class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sett = set(["+","-","/","*"])
        for token in tokens:
            if token not in sett:
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                match token:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":   
                        stack.append(a * b)
                    case "/":
                        stack.append(a / b)
        return int(stack[-1])
            

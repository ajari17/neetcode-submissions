class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        stack = []
        for token in tokens:
            if token != "+" and token != "-" and token != "*" and token != "/":
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
            

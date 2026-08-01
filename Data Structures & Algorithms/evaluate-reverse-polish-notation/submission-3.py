class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] != "+" and tokens[i] != "-" and tokens[i] != "*" and tokens[i] != "/":
                stack.append(tokens[i])
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                match tokens[i]:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":   
                        stack.append(a * b)
                    case "/":
                        stack.append(a / b)
            i += 1

        return int(stack[-1])
            

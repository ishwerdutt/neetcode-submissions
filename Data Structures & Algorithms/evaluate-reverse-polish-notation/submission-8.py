class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
               
            elif tokens[i] == "*":
                x = stack.pop()
                y = stack.pop()
                
                
                stack.append(x*y)
                

            elif tokens[i] == "/":
                x = stack.pop()
                y = stack.pop()
                
                stack.append(int(y/x))
                

            elif tokens[i] == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
                
                

            else:
                stack.append(int(tokens[i]))

        return stack[-1]
      
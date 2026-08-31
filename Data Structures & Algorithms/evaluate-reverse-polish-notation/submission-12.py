class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for i in range(0, len(tokens)):
            if tokens[i].lstrip('-').isnumeric():
                stack.append(int(tokens[i]))
            else:
                num1 = (stack.pop())
                num2 = (stack.pop())
                if tokens[i] == '+':
                    res = num1 + num2
                elif tokens[i] == '-':
                    res = num2 - num1
                elif tokens[i] == '*':
                    res = num1 * num2
                else:
                    res = int(num2 / num1)

                stack.append(res)
        

        return stack[0]
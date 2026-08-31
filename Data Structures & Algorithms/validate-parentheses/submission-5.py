class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        if len(s) <= 1:
            return False

        for char in s:
            if char in brackets:
                # it's a closing bracket
                if len(stack) > 0 and brackets[char] == stack[-1]:
                    # check top of stack
                    stack.pop()
                else:
                    # it's not in proper order
                    return False
            else:
                # it's an opening bracket
                stack.append(char)

        return True if len(stack) == 0 else False
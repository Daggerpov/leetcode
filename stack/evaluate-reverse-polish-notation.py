"""
Easy, just look at code. Append digit. If operator, then pop the last two digits and append the resulting operation.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            # means there must be two numbers (operands) before this operator
            if char == "+":
                num_right = stack.pop()
                num_left = stack.pop() # left goes second, since stack pops right -> left
                stack.append(int(num_left + num_right))
            elif char == "-":
                num_right = stack.pop()
                num_left = stack.pop() # left goes second, since stack pops right -> left
                stack.append(int(num_left - num_right))
            elif char == "*":
                num_right = stack.pop()
                num_left = stack.pop() # left goes second, since stack pops right -> left
                stack.append(int(num_left * num_right))
            elif char == "/":
                num_right = stack.pop()
                num_left = stack.pop() # left goes second, since stack pops right -> left
                stack.append(int(num_left / num_right))
            else:
                # operand, a.k.a. number
                stack.append(int(char))
        return int(stack[0]) # Eventually, I'll squash operators + operands into just one number (operand)

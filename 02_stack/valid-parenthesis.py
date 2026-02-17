class Solution:
    def isValid(self, s: str) -> bool:
        corresponding_parentheses = {')': '(', '}': '{', ']': '['}
        
        par_stack = []

        for parenthesis in s:
            if parenthesis in corresponding_parentheses.values():
                # this means parenthesis is an opening parenthesis
               par_stack.append(parenthesis)
            else: 
                # parenthesis is a closing parenthesis

                if par_stack and corresponding_parentheses[parenthesis] == par_stack[-1]:
                    par_stack.pop()
                else:
                    return False
        return True if not par_stack else False

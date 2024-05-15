class Solution(object):
    def isValid(self, s):
        stack = []
        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
            else:
                if not stack or (bracket == ')' and stack[-1] != '(') or (bracket == '}' and stack[-1] != '{') or (bracket == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return not stack

        
        
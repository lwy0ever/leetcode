class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(',']':'[','}':'{'}
        stack = []
        for c in s:
            if c in pair:
                if stack and stack[-1] == pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
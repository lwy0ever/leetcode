class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {'(':')','[':']','{':'}'}
        for c in s:
            if c in p:
                stack.append(c)
            else:
                if not stack:
                    return False
                if p[stack.pop()] != c:
                    return False
        return len(stack) == 0
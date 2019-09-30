class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        counter = 0
        ans = []
        for c in S:
            if c == '(':
                if counter > 0:
                    ans.append(c)
                counter += 1
            elif c == ')':
                if counter > 1:
                    ans.append(c)
                counter -= 1
        return ''.join(ans)

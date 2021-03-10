class Solution:
    def makeGood(self, s: str) -> str:
        ans = ['0']
        for c in s:
            if ans[-1].lower() == c.lower() and \
            (ans[-1].islower() and c.isupper() \
             or ans[-1].isupper() and c.islower()):
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans[1:])
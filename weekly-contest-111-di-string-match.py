class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = len(S)
        l = 0
        r = n
        ans = []
        for c in S:
            if c == 'I':
                ans.append(l)
                l += 1
            else:
                ans.append(r)
                r -= 1
        ans.append(l)
        return ans
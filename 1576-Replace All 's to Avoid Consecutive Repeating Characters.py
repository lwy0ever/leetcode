class Solution:
    def modifyString(self, s: str) -> str:
        ans = []
        n = len(s)
        alphabet = range(ord('a'),ord('z') + 1)
        for i,c in enumerate(s):
            if c != '?':
                ans.append(c)
                continue
            neared = set()
            if ans:
                neared.add(ans[-1])
            if i + 1 < n:
                neared.add(s[i + 1])
            for ind in alphabet:
                if chr(ind) not in neared:
                    ans.append(chr(ind))
                    break
        return ''.join(ans)
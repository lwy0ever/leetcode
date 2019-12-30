class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        ws = str.split()
        if len(ws) != len(pattern):
            return False
        d = {}
        p = {}
        for i,c in enumerate(pattern):
            if c not in d and ws[i] not in p:
                d[c] = ws[i]
                p[ws[i]] = c
            else:
                if c in d and d[c] != ws[i] or ws[i] in p and p[ws[i]] != c:
                    return False
        return True
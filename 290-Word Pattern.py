class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        ws = str.split()
        if len(ws) != len(pattern):
            return False
        d = dict()  # pattern -> str
        p = dict()  # str -> pattern
        for i,c in enumerate(pattern):
            if (c in d and d[c] != ws[i]) or (ws[i] in p and p[ws[i]] != c):
                return False
            d[c] = ws[i]
            p[ws[i]] = c
        return True
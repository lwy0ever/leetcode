class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        cnt = [0] * 26
        for i in range(n):
            cnt[(ord(t[i]) - ord(s[i])) % 26] += 1
        d,m = divmod(k,26)
        #print(cnt,d,m)
        for i in range(1,26):
            if i <= m:
                if d + 1 < cnt[i]:
                    return False
            else:   # i > m
                if d < cnt[i]:
                    return False
        return True
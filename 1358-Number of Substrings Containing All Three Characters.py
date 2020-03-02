class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        l = 0
        r = 0
        cnt = {'a':0,'b':0,'c':0}
        while r < n:
            cnt[s[r]] += 1
            r += 1
            while cnt['a'] > 0 and cnt['b'] > 0 and cnt['c'] > 0:
                ans += n - r + 1
                #print(l,r,n - r + 1)
                cnt[s[l]] -= 1
                l += 1
        return ans
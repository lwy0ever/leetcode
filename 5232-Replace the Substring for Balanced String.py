class Solution:
    def balancedString(self, s: str) -> int:
        d = collections.Counter()
        for c in s:
            d[c] += 1
        n = len(s) // 4
        for k in 'QWER':
            d[k] -= n
        d = +d
        #print(d)
        if len(d) == 0:
            return 0
        ap = collections.Counter()
        ans = n * 4
        l = 0
        r = 1
        ap[s[0]] = 1
        while r <= n * 4:
            #print(d,ap,l,r,+(d - ap))
            if +(d - ap):
                if r == n * 4:
                    break
                ap[s[r]] += 1
                r += 1
            else:
                ans = min(ans,r - l)
                ap[s[l]] -= 1
                l += 1
                if r < l:
                    r = l
        return ans
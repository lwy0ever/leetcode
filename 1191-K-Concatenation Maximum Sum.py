class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        ans = 0
        # arr本身最大数组
        s = 0
        ttl = 0
        for a in arr:
            if s + a >= 0:
                s += a
                ans = max(ans,s)
            else:
                s = 0
            ttl += a
        #print(s)
        ans = max(ans,s)
        s = 0
        l = 0
        for a in arr:
            s += a
            l = max(l,s)
        s = 0
        r = 0
        for a in arr[::-1]:
            s += a
            r = max(r,s)
        #if  r == ttl:
        #    r = 0
        ans = max(ans,l + r,ttl * (k - 2) + l + r)
        return ans % (10 ** 9 + 7)
            
class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        n = len(h)
        l = 0
        r = n - 1
        ll = rr = 0
        ans = 0
        while l < r:
            if h[l] < h[r]:
                if ll > h[l]:
                    ans += ll - h[l]
                else:
                    ll = h[l]
                l += 1
            else:
                if rr > h[r]:
                    ans += rr - h[r]
                else:
                    rr = h[r]
                r -= 1
        return ans
        '''
        while l < r:
            if h[l] < h[r]:
                ll = l
                l += 1
                s = 0
                while h[l] < h[ll]:
                    s += h[l]
                    l += 1
                ans += h[ll] * (l - ll - 1) - s
            else:
                rr = r
                r -= 1
                s = 0
                while h[r] < h[rr]:
                    s += h[r]
                    r -= 1
                ans += h[rr] * (rr - r - 1) - s
        return ans
        '''
                    
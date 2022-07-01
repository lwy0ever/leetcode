class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 二分查找
        n = len(piles)

        def tryToEat(k):
            ttl = 0
            for p in piles:
                ttl += (p - 1) // k + 1
            return ttl <= h

        # 由于h >= len(piles),所以最大为max(piles)
        l = max(sum(piles) // h,1)
        r = max(piles)
        ans = float('inf')
        while l <= r:
            m = (l + r) // 2
            #print(m)
            if tryToEat(m):
                #print(f'{m} ok')
                ans = min(ans,m)
                r = m - 1
            else:
                l = m + 1
        return ans
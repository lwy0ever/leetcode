class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # 如果每个小时吃k个,是否可以吃完
        def possible(k):
            s = 0
            for p in piles:
                s += (p - 1) // k + 1
            return s <= H
        
        # 二分查找最小值
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            if possible(m):
                r = m
            else:
                l = m + 1
        return l
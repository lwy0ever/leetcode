class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # 二分查找
        def shipDays(ability):
            days = 1
            shipped = 0
            for w in weights:
                if shipped + w <= ability:
                    shipped += w
                else:
                    days += 1
                    shipped = w
            return days
        n = len(weights)
        l = max(weights)
        r = sum(weights)
        if D >= n:
            return l
        while l < r:
            mid = (l + r) // 2
            #print(l,mid,r,shipDays(mid))
            if shipDays(mid) <= D:
                r = mid
            else:
                l = mid + 1
        return l
        
        
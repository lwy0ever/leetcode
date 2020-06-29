class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        
        def check(day):
            flower = 0
            cnt = 0
            for i in range(n):
                if bloomDay[i] <= day:
                    cnt += 1
                else:
                    flower += cnt // k
                    cnt = 0
            flower += cnt // k
            return flower

        days = sorted(set(bloomDay))
        l = 0
        r = len(days) - 1
        # 二分查找
        while l <= r:
            mid = (l + r) // 2
            day = days[mid]
            if check(day) >= m:
                r = mid - 1
            else:
                l = mid + 1
        return days[l]
            
            
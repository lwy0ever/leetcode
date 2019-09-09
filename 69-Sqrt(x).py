class Solution:
    def mySqrt(self, x: int) -> int:
        # 牛顿法
        if x <= 1:
            return x
        t = 1
        while True:
            pre = t
            t = (t + x / t) / 2
            if abs(t - pre) < 1e-6:
                return int(t)
        # 二分法
        '''
        if x <= 1:
            return x
        l = 0
        h = x
        while True:
            t = (l + h) // 2
            if t ** 2 <= x and (t + 1) ** 2 > x:
                return t
            if t ** 2 < x:
                l = t + 1
            else:
                h = t
        '''
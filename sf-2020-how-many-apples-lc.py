class Solution:
    def findNum(self, n: int, k: int) -> int:
        # 原有r * n + k
        # 取走r * k + k
        # 剩余r * (n - k) + k
        # 也就是说,(原数字 - k) * (n - k) = (新数字 - k) * n
        # 找到n和n - k的最大公约数g,每次递增n // g倍...
        # 没想明白
        mod = 10 ** 9 + 7
        from math import gcd
        res = 1
        g = gcd(n,n - k)
        t = n // g
        for i in range(n):
            res = res * t % mod
        return (res * n - n + k) % mod
        '''
        # 上一次有n * m + k个,拿走k * m + k个,剩余(n - k) * m个
        # 本次有(n - k) * m,则上一次有n * m + k
        init = 0
        while True:
            m = init
            #ans = m * (n - k)
            for i in range(n + 1):
                ans = n * m + k
                if ans % (n - k) != 0:
                    break
                m = ans // (n - k)
                #print(i,ans)
            else:
                return ans % (10 ** 9 + 7)
            init += 1
        '''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            p = - n
        else:
            p = n
        
        def mp(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            t = mp(x,n // 2)
            if n & 1 == 0:
                return t * t
            else:
                return t * t * x
        
        if n >= 0:
            return mp(x,p)
        else:
            return 1 / mp(x,p)
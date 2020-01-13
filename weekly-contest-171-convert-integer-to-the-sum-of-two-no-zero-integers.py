class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def noZero(n):
            while n >= 10:
                if n % 10 == 0:
                    return False
                n //= 10
            return True

        for i in range(1,n):
            if noZero(i) and noZero(n - i):
                return [i,n - i]
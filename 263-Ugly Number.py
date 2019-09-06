class Solution:
    def isUgly(self, num: int) -> bool:
        # Input is within the 32-bit signed integer range: [−2 ** 31,  2 ** 31 − 1]
        if num <= 0:
            return False
        primes = [2,3,5]
        for p in primes:
            while num % p == 0:
                num //= p
        return num == 1
        '''
        if num <= 0:
            return False
        primes = [2,3,5]
        while num > 1:
            for p in primes:
                if num % p == 0:
                    num //= p
                    break
            else:
                return False
        return True
        '''
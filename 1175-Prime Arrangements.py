class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # 先统计质数数量p
        # 则可能的方案数量=p! * (n - p)!
        if n <= 2:
            return 1
        
        primes = [] # 不考虑偶数
        def isPrime(n):
            for p in primes:
                if n % p == 0:
                    return False
            return True

        p = 1   # 考虑2
        for i in range(3,n + 1,2):
            if isPrime(i):
                primes.append(i)
                p += 1
        #print(p)
        return reduce(lambda x,y: x * y,range(1,p + 1)) * reduce(lambda x,y: x * y,range(1,n - p + 1)) % (10 ** 9 + 7)
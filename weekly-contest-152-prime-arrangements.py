class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 1
        num = 1
        for e in range(3,n + 1,2):
            for i in range(3,int(e ** 0.5) + 1,2):
                if e % i == 0:
                    break
            else:
                num += 1
        print(num)
        a = 1
        for i in range(1,num + 1):
            a *= i
        b = 1
        for i in range(1,n - num + 1):
            b *= i
        return (a * b) % (10 ** 9 + 7)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        isPrime = [1] * n   #立flag
        #设置0和1位为0
        isPrime[0] = isPrime[1] = 0
        # 特殊处理2,以便step可以变为2(貌似意义不是太大)
        for i in range(4,n,2):
            isPrime[i] = 0
        #下面的思路是在 3 到 n ** 0.5 的范围内，当一个数是质数，将它所有的比n小的倍数设置成0
        for i in range(3,int(n ** 0.5) + 1,2):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n - 1) // i - i + 1)
        #print(isPrime)
        #现在每个质数位的flag为1，其余的位数为0.由于我们不需要知道质数是什么只要总数，因此直接返回list里面所有1的和就行。
        return sum(isPrime)
        '''
        if n < 3:
            return 0
        if n == 3:
            return 1
        prime = []
        i = 3
        while i < n:
            for p in prime:
                if i % p == 0:
                    break
                if p * p >= i:
                    prime.append(i)
                    break
            else:
                prime.append(i)
            i += 2
        return len(prime) + 1   # 加上质数2
        '''

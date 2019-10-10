class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        # 由于10 ** 6 = 11110100001001000000,共20位
        # 因此可能的质数一定在2-19之间
        prime = {2,3,5,7,11,13,17,19}
        
        # 计算x的二进制数中1的个数
        def count1(x):
            cnt = 0
            while x > 0:
                x &= (x - 1)
                cnt += 1
            return cnt
        
        ans = 0
        for i in range(L,R + 1):
            if count1(i) in prime:
                ans += 1
        return ans
class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n & 1 == 0:
                n >>= 1
            else:
                # n % 4 == 1时减1
                # n % 4 == 3时加1
                # 有个例外是3, 3——2——1 比 3——4——2——1更快
                if n & 2 == 0:
                    n -= 1
                else:   # n & 2 == 2:
                    if n == 3:
                        n -= 1
                    else:
                        n += 1
            ans += 1
        return ans
        '''
        if n == 1:
            return 0
        elif n & 1 == 0:
            return self.integerReplacement(n // 2) + 1
        else:
            return min(self.integerReplacement(n + 1),self.integerReplacement(n - 1)) + 1
        '''
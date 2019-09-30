class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return '0'
        
        # 与整数转换思路相同，不过取模时取-2
        ans = ''
        while N != 0:
            if N % 2 == 0:
                ans = '0' + ans
                N /= -2
            else:
                ans = '1' + ans
                N = (N - 1) / (-2)
        return ans
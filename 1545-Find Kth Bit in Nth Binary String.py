class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # 方法1:找规律
        # 对于Sn来说,Sn = S(n-1) + '1' + 反转(取反S(n - 1))
        # Sn的长度 = len(S(n - 1)) * 2 + 1 = 2 ** n - 1
        # 对于findKthBit(n,k)
        # 如果k == 1,则为'0'
        # 如果k == 2 ** (n - 1),则findKthBit(n,k) = 1
        # 如果k <= 2 ** (n - 1) - 1,则findKthBit(n,k) = findKthBit(n - 1,k)
        # 如果k > 2 ** n,则findKthBit(n,k) = findKthBit(n - 1,2 ** n - k)取反
        if k == 1:
            return '0'
        if k == 2 ** (n - 1):
            return '1'
        if k < 2 ** (n - 1):
            return self.findKthBit(n - 1,k)
        else:
            return '1' if self.findKthBit(n - 1,2 ** n - k) == '0' else '0'
        # 方法2:无脑算法
        '''
        s = '0'
        for i in range(n):
            t = ['1' if c == '0' else '0' for c in s]
            s += '1' + ''.join(t[::-1])
            if len(s) >= k:
                return s[k - 1]
        '''
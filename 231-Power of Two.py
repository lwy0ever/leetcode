class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 2的幂,二进制表示一定只有1个1
        return n > 0 and n & (n - 1) == 0
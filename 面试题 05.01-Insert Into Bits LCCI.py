class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        if M >= N:return M
        mask1 = 2 ** 32 - 1
        mask0 = 2 ** (j - i + 1) - 1
        mask = mask1 ^ (mask0 << i)
        return (N & mask) | (M << i)
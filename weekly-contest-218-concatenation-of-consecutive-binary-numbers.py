class Solution:
    def concatenatedBinary(self, n: int) -> int:
        m = 10 ** 9 + 7
        ans = 0
        size = 0
        for i in range(1,n + 1):
            if i & (i - 1) == 0:    # 进位了
                size += 1
            ans = ((ans << size) + i) % m
        return ans
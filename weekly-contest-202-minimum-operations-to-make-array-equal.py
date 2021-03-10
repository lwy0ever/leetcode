class Solution:
    def minOperations(self, n: int) -> int:
        # 最终目标是(1 + (2 * (n - 1) + 1)) / 2 => n
        # 所以arr[0] = 1,需要操作n - 1次
        # arr[1] = 3,需要操作n - 3次
        # ...
        if n & 1:   # 奇数
            # 需要n-1次,n-3次...2次,0次
            return ((n - 1) + 2) * (n // 2) // 2
        else:   # 偶数
            # 需要n-1次,n-3次...3次,1次
            return ((n - 1) + 1) * (n // 2) // 2
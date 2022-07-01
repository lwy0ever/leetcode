class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        # 个位2出现的次数=n // 10 * 1 + min(1,n % 10 - 2 + 1 if n % 10 >= 2 else 0)
        # 十位出现的次数=n // 100 * 10 + min(10,n % 100 - 20 + 1 if n % 100 >= 20 else 0)
        # ...
        ans = 0
        big = 10
        small = 1
        while n >= small:
            ans += n // big * small + min(small,n % big - 2 * small + 1 if n % big >= 2 * small else 0)
            big *= 10
            small *= 10
        return ans
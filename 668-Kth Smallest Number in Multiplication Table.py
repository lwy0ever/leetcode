class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # 一共有m * n个数
        # 最大的数是m * n,最小的数是1
        # 其中有些数字重复,有些数字缺失
        # 如果某个数字,有k个数字小于等于它,则它是第k个
        # 实际上
        # 对于某个数字x,可能有s个数字小于它(s < k)
        # 对于数字x + 1,可能有s + t个数字小于它(设s + t >= k),其中t >= 1
        # 那么找到数字x即可

        # 对于数字x,比x小的数有
        # 第1行:min(ceil(x / 1),n)
        # 第2行:min(ceil(x / 2),n)
        # ...
        # 第m行:min(ceil(x / m),n)
        # 当ceil(x / i) >= n时,取值为n,满足条件的i <= ceil(x / n)
        # 所以,对于前ceil(x / n)行,整行都满足
        return bisect.bisect_left(range(m * n),k,key = lambda x:n * (x // n) + sum(x // i for i in range(x // n + 1,m + 1)))
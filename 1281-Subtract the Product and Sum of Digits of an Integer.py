class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        s = 0
        while n:
            n,m = divmod(n,10)
            mul *= m
            s += m
        return mul - s
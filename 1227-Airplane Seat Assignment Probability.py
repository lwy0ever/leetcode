class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # n = 1,100%
        # n = 2,第1个人坐1的概率50%,则第2个人坐2的概率是50%
        # n = n
        # 有1/n的概率,第1个人坐了1,则n坐n的概率是100%
        # 有1/n的概率,第1个人坐了n,则2到n-1都坐正确,n坐1
        # 有(n - 2)/n的概率,第1个人坐到了i(1 < i < n),则2到i - 1都可以坐正确,第i个人在n - (i - 1)个座位里面选择
        # 然后推导(见官方答案)
        return 1 if n == 1 else 0.5
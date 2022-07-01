class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        # 第1位为1-9(9种选择),第2位可以从0-9种选择除第1位的(9种选择),第3位8种选择...
        # 如果第1位为0,则取n-1的结果
        ans = 9
        for i in range(2,n + 1):
            ans *= (11 - i)
        ans += self.countNumbersWithUniqueDigits(n - 1)
        return ans
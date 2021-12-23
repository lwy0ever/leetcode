class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ma = int((c // 2) ** 0.5)
        for x in range(ma + 1):
            y2 = c - x ** 2
            if int(y2 ** 0.5) ** 2 == y2:
                return True
        return False
class Solution:
    def printBin(self, num: float) -> str:
        if num < 0 or num >= 1:
            return 'ERROR'
        ans = '0.'
        for i in range(30):
            if num == 0.0:
                return ans
            num *= 2
            if num >= 1:
                ans += '1'
                num -= 1
            else:
                ans += '0'
        if num == 0.0:
            return ans
        return 'ERROR'
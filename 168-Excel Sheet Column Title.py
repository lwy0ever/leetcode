class Solution:
    def convertToTitle(self, n: int) -> str:
        # ord('A') = 65
        ans = ''
        while n:
            n -= 1
            n,m = divmod(n,26)
            ans = chr(65 + m) + ans
        return ans
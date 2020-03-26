class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 回文串可以由n个偶数字符 + 0 or 1个奇数字符组成
        cnt = collections.Counter(s)
        ans = 0
        hasOdd = False
        for v in cnt.values():
            if v & 1 == 0:
                ans += v
            else:
                ans += v - 1
                hasOdd = True
        if hasOdd:
            ans += 1
        return ans
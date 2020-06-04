class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 从中间向两边扩展
        def extend(s,l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1,r - 1

        # 从中间向两边扩展
        ansL,ansR = 0,0
        n = len(s)
        for i in range(n):
            # 选定中间位置
            l,r = extend(s,i,i)
            if r - l > ansR - ansL:
                ansL,ansR = l,r
            l,r = extend(s,i,i + 1)
            if r - l > ansR - ansL:
                ansL,ansR = l,r
        return s[ansL:ansR + 1]            
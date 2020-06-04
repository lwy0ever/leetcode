class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(l,r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        n = len(s)
        # 从两端逐字符比对
        l = 0
        r = n - 1
        while l < r:
            if s[l] == s[r]:    # 如果对称,则向中间靠拢
                l += 1
                r -= 1
            else:
                # 否则尝试删掉s[l]或者s[r]
                return checkPalindrome(l + 1,r) or checkPalindrome(l,r - 1)
        return True
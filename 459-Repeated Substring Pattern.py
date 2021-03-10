class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 方法2:如果s满足条件,那么将两个s连在一起,并移除第一个和最后一个字符,那么得到的字符串一定包含s,即s是它的一个子串
        return (s + s).find(s,1) != len(s)

        # 方法1:
        # 如果可以,则子串一定是从s[0]开始的
        n = len(s)
        for l in range(1,n // 2 + 1):
            if n % l != 0:
                continue
            for start in range(1,n // l):
                if s[:l] != s[start * l:(start + 1) * l]:
                    break
            else:
                return True
        return False
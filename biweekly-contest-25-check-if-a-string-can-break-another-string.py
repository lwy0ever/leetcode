class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        cnt1 = collections.Counter(s1)
        cnt2 = collections.Counter(s2)
        c1 = [0] * 26
        c2 = [0] * 26
        for k,v in cnt1.items():
            c1[ord(k) - ord('a')] = v
        for k,v in cnt2.items():
            c2[ord(k) - ord('a')] = v
        s1 = 0
        s2 = 0
        sign = 0
        for i in range(26):
            s1 += c1[i]
            s2 += c2[i]
            if (s1 > s2 and sign == -1) or (s1 < s2 and sign == 1):
                return False
            if sign == 0:
                if s1 > s2:
                    sign = 1
                if s1 < s2:
                    sign = -1
        return True
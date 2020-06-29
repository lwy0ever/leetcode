class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        if n < m:
            return []
        ans = []
        base = ord('a')
        arrP = [0] * 26
        for c in p:
            arrP[ord(c) - base] += 1
        arrS = [0] * 26
        for c in s[:m]:
            arrS[ord(c) - base] += 1
        if arrP == arrS:
            ans.append(0)
        for i in range(m,n):
            arrS[ord(s[i - m]) - base] -= 1
            arrS[ord(s[i]) - base] += 1
            if arrP == arrS:
                ans.append(i - m + 1)
        return ans
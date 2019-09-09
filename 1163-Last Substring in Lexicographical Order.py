class Solution:
    def lastSubstring(self, s: str) -> str:
        maxC = 'a'
        ps = []
        n = len(s)
        for i in range(n):
            if s[i] == maxC:
                ps.append(i)
            elif s[i] > maxC:
                maxC = s[i]
                ps = [i]
        #print(maxC,ps)
        ans = ''
        for p in ps:
            if s[p:n] > ans:
                ans = s[p:n]
        return ans
                
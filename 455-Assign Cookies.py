class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        n = len(s)
        if n == 0:
            return 0
        #print(g)
        #print(s)
        ans = 0
        sInd = 0
        for gi in g:
            #print(gi,s[sInd])
            if s[sInd] >= gi:
                ans += 1
                sInd += 1
            if sInd == n:
                return ans
        return ans
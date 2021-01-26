class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 方法1:
        # 胃口从小到大
        # 饼干从小到大
        # 逐个饼干检查,如果当前胃口可以满足,则满足之
        g.sort()
        s.sort()
        n = len(g)
        if n == 0:
            return 0
        ans = 0
        gInd = 0
        for size in s:
            if size >= g[gInd]:
                ans += 1
                gInd += 1
                if gInd == n:
                    return ans
        return ans

        '''
        # 方法2:
        # 胃口从大到小
        # 饼干从大到小
        # 逐个胃口检查,如果当前的饼干可以满足,则满足之
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
        '''
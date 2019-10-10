class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        d = {}
        for w in words:
            t = d
            for c in w[::-1]:
                if c not in t:
                    t[c] = {}
                t = t[c]
        ans = 0
        def dfs(d,l):
            if not d:
                nonlocal ans
                ans += l
                return
            for k in d.keys():
                dfs(d[k],l + 1)
        
        #print(d)
        for k in d.keys():
            dfs(d[k],2) #末位 + #,所以是2位
        return ans
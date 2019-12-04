class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        mi = 99999999
        ma = 0
        for w in wordDict:
            mi = min(mi,len(w))
            ma = max(ma,len(w))
        #print(dl)
        dic = set(wordDict)
        n = len(s)
        #ans = []
        cache = {n:['']} #结尾返回
        
        def dfs(i): # 返回s[i:]的组合方案
            #print(cache)
            if i in cache:
                return cache[i]
            ans = []
            for j in range(i + mi,min(i + ma,n) + 1):
                if s[i:j] in dic:
                    ans.extend(list(map(lambda x:s[i:j] + ' ' + x,dfs(j))))
                    #print(s[i:j],ans)
            cache[i] = ans
            #print(cache)
            return cache[i]

        #dfs(0)
        #print(cache)
        return [s[:-1] for s in dfs(0)]
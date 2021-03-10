from collections import Counter
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        nw = len(words)
        nsc = {}
        for i in range(26):
            nsc[chr(97 + i)] = score[i]
        #print(nsc)
        
        cnts = []
        scs = []
        for w in words:
            cnts.append(Counter(w))
            t = 0
            for c in w:
                t += nsc[c]
            scs.append(t)
            
        cntL = Counter(letters)
        
        ans = 0
        def dfs(iw,cnt,sc):
            if iw == nw:
                return
            if len(+(cnts[iw] - cnt)) == 0:
                nonlocal ans
                ans = max(ans,sc + scs[iw])
                dfs(iw + 1,cnt - cnts[iw],sc + scs[iw])
            dfs(iw + 1,cnt,sc)
        dfs(0,cntL,0)
        return ans
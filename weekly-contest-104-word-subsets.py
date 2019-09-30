class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        maxChrB = collections.defaultdict(int)
        for b in set(B):
            cntB = collections.Counter(b)
            for c,v in cntB.items():
                maxChrB[c] = max(maxChrB[c],v)
        ans = []
        for a in A:
            cnt = collections.Counter(a)
            for c,v in maxChrB.items():
                if cnt[c] < v:
                    break
            else:
                ans.append(a)
        return ans
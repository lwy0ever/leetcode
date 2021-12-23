class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        score_pos = []
        for i,s in enumerate(score):
            score_pos.append((i,s))
        score_pos.sort(key = lambda x:x[1],reverse = True)
        ans = [''] * n
        for i,p in enumerate(score_pos):
            if i == 0:
                ans[p[0]] = 'Gold Medal'
            elif i == 1:
                ans[p[0]] = 'Silver Medal'
            elif i == 2:
                ans[p[0]] = 'Bronze Medal'
            else:
                ans[p[0]] = str(i + 1)
        return ans
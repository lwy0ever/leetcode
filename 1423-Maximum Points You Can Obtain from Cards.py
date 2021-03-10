class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        s = sum(cardPoints[-k:])
        ans = s
        #print(s)
        for i in range(k):
            s += cardPoints[i] - cardPoints[- k + i]
            ans = max(ans,s)
            #print(s)
        return ans
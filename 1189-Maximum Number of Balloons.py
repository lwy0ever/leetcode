class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = float('inf')
        cnt = collections.Counter(text)
        t = collections.Counter('balloon')
        for k in t:
            ans = min(ans,cnt[k] // t[k])
        return ans
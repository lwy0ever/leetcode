class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = {'a','e','i','o','u'}
        ans = 0
        for c in s[:k]:
            if c in v:
                ans += 1
        cnt = ans
        for i in range(len(s) - k):
            if s[i] in v:
                cnt -= 1
            if s[i + k] in v:
                cnt += 1
            ans = max(ans,cnt)
        return ans
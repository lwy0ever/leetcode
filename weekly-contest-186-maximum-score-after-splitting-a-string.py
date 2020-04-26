class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            left = 1
        else:
            left = 0
        right = 0
        for i in range(1,n):
            if s[i] == '1':
                right += 1
        ans = left + right
        for i in range(1,n - 1):
            if s[i] == '0':
                left += 1
            else:
                right -= 1
            ans = max(ans,left + right)
        return ans
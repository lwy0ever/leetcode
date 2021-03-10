class Solution:
    def countSubstrings(self, s: str) -> int:
        # 如果s[i:j]是回文串,则s[i + 1:j - 1],s[i + 2:j - 2]...也是
        n = len(s)
        mid = [False] * (n * 2) # 记录(i + j),相当于s[i:j]的中间位置的2倍,以避免重复
        ans = 0
        for i in range(n):
            for j in range(n,i,-1):
                if not mid[i + j] and s[i:j] == s[i:j][::-1]:
                    mid[i + j] = True
                    ans += (j - i + 1) // 2
        return ans
class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return S
        ans = ''
        pre = S[0]
        cnt = 1
        for c in S[1:] + '#':
            if c == pre:
                cnt += 1
            else:
                ans += pre + str(cnt)
                pre = c
                cnt = 1
        if len(ans) < len(S):
            return ans
        else:
            return S
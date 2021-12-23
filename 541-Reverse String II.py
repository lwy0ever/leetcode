class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        ans = []
        reverse = True
        for i in range(0,n,k):
            if reverse:
                ans.append(s[i:i + k][::-1])
            else:
                ans.append(s[i:i + k])
            reverse = not reverse
        return ''.join(ans)
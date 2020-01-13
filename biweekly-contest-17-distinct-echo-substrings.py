class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        ans = set()
        n = len(text)
        for i in range(n - 1):
            for j in range(i + 1,n):
                if j - i > n - j:
                    break
                if text[i:j] == text[j:j * 2 - i]:
                    ans.add(text[i:j])
        return len(ans)
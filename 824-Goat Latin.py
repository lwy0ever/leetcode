class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans = sentence.split()
        for i,w in enumerate(ans):
            if w[0].lower() not in ('a','e','i','o','u'):
                ans[i] = w[1:] + w[0]
            ans[i] += 'ma'
            ans[i] += 'a' * (i + 1)
        return ' '.join(ans)
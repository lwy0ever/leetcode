class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        di = dict(zip('abcdefghijklmnopqrstuvwxyz','22233344455566677778889999'))
        n = len(num)
        ans = []
        for w in words:
            for i in range(n):
                if di[w[i]] != num[i]:
                    break
            else:
                ans.append(w)
        return ans
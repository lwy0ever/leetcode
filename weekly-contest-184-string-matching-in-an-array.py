class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for w in words:
            for f in words:
                if w == f:
                    continue
                if f.find(w) >= 0:
                    ans.append(w)
                    break
        return ans
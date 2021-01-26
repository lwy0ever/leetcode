class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = collections.Counter(A[0])
        for s in A:
            t = collections.Counter(s)
            ans -= ans - t
        return list(ans.elements())
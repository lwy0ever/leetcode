class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        m = 0
        for x in A:
            d,m = divmod((m << 1) + x,5)
            if m == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
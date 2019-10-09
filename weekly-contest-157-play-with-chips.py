class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        d = {0:0,1:0}
        for c in chips:
            if c & 1 == 0:
                d[0] += 1
            else:
                d[1] += 1
        return min(d[0],d[1])
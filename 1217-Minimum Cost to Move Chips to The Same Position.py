class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # 同奇偶位置移动,cost = 0
        # 不同奇偶位置移动,cost = 1
        odd = 0
        even = 0
        for p in position:
            if p & 1:
                odd += 1
            else:
                even += 1
        return min(odd,even)
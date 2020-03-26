class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0] or  # A在B左侧
                    rec1[3] <= rec2[1] or  # A在B下方
                    rec1[0] >= rec2[2] or  # A在B右侧
                    rec1[1] >= rec2[3])    # A在B上方
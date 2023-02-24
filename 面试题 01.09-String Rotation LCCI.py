class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        # 比如xy旋转之后变为yx
        # 那么如果将xy自身连接,变成xyxy,那么xyxy会包含yx
        return len(s1) == len(s2) and (s1 + s1).find(s2) >= 0
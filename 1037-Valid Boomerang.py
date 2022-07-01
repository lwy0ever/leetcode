class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # 不相同
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        # 水平线
        if points[0][0] == points[1][0] == points[2][0]:
            return False
        if points[0][0] != points[1][0]:    # 点0和点1非水平
            return (points[0][1] - points[1][1]) * (points[0][0] - points[2][0]) != (points[0][0] - points[1][0]) * (points[0][1] - points[2][1])
        else:
            # 点0和点1水平,点2非水平
            return True

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1 = coordinates[0]
        x2,y2 = coordinates[1]
        if x2 - x1 == 0:
            for c in coordinates[2:]:
                if c[0] != x1:
                    return False
            return True
        else:
            t = (y2 - y1) / (x2 - x1)
            for c in coordinates[2:]:
                if (c[1] - y1) / (c[0] - x1) != t:
                    return False
            return True
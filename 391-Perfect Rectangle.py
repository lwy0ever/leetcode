class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 构成大矩形的小矩形,顶点会重合,并且重合次数为偶数次(2次or4次)
        # 只有大矩形的4个顶点没有重合的情况
        # 存储大矩形的左下角和右上角
        xmin = float('inf')
        ymin = float('inf')
        xmax = float('-inf')
        ymax = float('-inf')
        points = set()  # 存储顶点
        area = 0    # 记录面积,避免重复覆盖的情况
        for x1,y1,x2,y2 in rectangles:
            xmin = min(xmin,x1)
            ymin = min(ymin,y1)
            xmax = max(xmax,x2)
            ymax = max(ymax,y2)
            
            area += (y2 - y1) * (x2 - x1)
            
            for p in [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)
        # 只剩下四个点并且是最大矩形的左下角和右上角
        if len(points) != 4:
            return False
        if (xmin,ymin) not in points or (xmin,ymax) not in points or (xmax,ymin) not in points or (xmax,ymax) not in points:
            return False
        # 判断面积
        if (ymax - ymin) * (xmax - xmin) != area:
            return False
        return True
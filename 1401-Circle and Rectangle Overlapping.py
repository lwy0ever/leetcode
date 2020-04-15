class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # 矩形4条边将空间分成9个区域(井字型)
        # 如果圆心在中间,则重叠
        if x1 <= x_center <= x2 and y1 <= y_center <= y2:
            return True
        # 如果圆心在上/下/左/右,则判断圆心+半径是否到达了矩形边界
        elif x_center > x2 and y1 <= y_center <= y2: # 右
            return radius >= x_center - x2
        elif y_center < y1 and x1 <= x_center <= x2: # 下
            return radius >= y1 - y_center
        elif x_center < x1 and y1<= y_center <= y2: # 左
            return radius >= x1 - x_center
        elif y_center > y2 and x1 <= x_center <= x2: # 上
            return radius >= y_center - y2
        else:
        # 如果圆心在左上/右上/左下/右下,则判断矩形的端点是否在圆内
            return min((x1 - x_center) ** 2 + (y2 - y_center) ** 2,\
                       (x2 - x_center) ** 2 + (y2 - y_center) ** 2, \
                       (x2 - x_center) ** 2 + (y1 - y_center) ** 2, \
                       (x1 - x_center) ** 2 + (y1 - y_center) ** 2) <= radius ** 2
        
class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        # 情况1:半径为r的圆最多只能圈中1个点,则该点与所有点的距离都大于2 * r
        # 情况2:半径为r的圆最多可以圈中2个点,则可以通过移动该圆,使2个点都在圆周上
        # 情况3:半径为r的圆最多可以圈中2个以上的点,则可以通过移动该圆,使至少2个点在圆周上,并且其余点依然在圆内(含圆周上)
        # 重点关注情况2,3,也就是说,有2个(或者以上)的点在圆周上的圆,是可能的方案
        # 问题转化为:任取2个点,找到圆周通过这2个点的圆(一般有2个),然后统计其内的点数
        def getDistance2(p1,p2): # 计算两点间距离的平方(为了减小开方误差,只在需要开方的时候才开方)
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        def getCenter(p1,p2,r):    # 计算圆心
            d2 = getDistance2(p1,p2)
            if d2 > (r * 2) ** 2:
                return False,None,None
            # p1和p2的中点记为[mx,my]
            # 圆心为[cx,cy]
            # (cx - mx) ** 2 + (cy - my) ** 2 = h ** 2
            # 根据向量关系, 垂直的充要条件是两个向量的点积为0
            # 也就是(p1[0] - p2[0]) * (cx - mx) + (p1[1] - p2[1]) * (cy - my) = 0
            # 解上面关于cx和cy的2个方程
            mx = (p1[0] + p2[0]) / 2
            my = (p1[1] + p2[1]) / 2
            dx, dy = p1[0] - p2[0], p1[1] - p2[1]
            h = math.sqrt(r ** 2 - d2 / 4)
            c1 = [mx + h * dy / math.sqrt(dx ** 2 + dy ** 2),my - h * dx / math.sqrt(dx ** 2 + dy ** 2) ]
            c2 = [mx - h * dy / math.sqrt(dx ** 2 + dy ** 2),my + h * dx / math.sqrt(dx ** 2 + dy ** 2) ]
            return True,c1,c2

        import math
        ans = 1 # 最少会有1个点在圆内
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1,n):
                canCross,c1,c2 = getCenter(points[i],points[j],r)
                #print(canCross,c1,c2)
                if canCross:
                    for c in [c1,c2]:
                        cnt = 0
                        for x in range(n):
                            if getDistance2(c,points[x]) <= r ** 2:
                                cnt += 1
                        #print(c,cnt)
                        ans = max(ans,cnt)
        return ans
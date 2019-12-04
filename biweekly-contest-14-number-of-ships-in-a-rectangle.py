# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if not sea.hasShips(topRight,bottomLeft):
            return 0
        
        ans = 1
        # bfs
        fromA = [(topRight,bottomLeft)]
        while fromA:
            toA = []
            for tr,bl in fromA:
                x1,y1 = tr.x,tr.y
                x0,y0 = bl.x,bl.y
                if x0 == x1 and y0 == y1:
                    continue
                xm = (x0 + x1) // 2
                ym = (y0 + y1) // 2
                ans -= 1
                if sea.hasShips(Point(xm,ym),Point(x0,y0)):
                    ans += 1
                    if ans >= 10:
                        return ans
                    toA.append((Point(xm,ym),Point(x0,y0)))
                if xm + 1 <= x1 and ym + 1 <= y1:
                    if sea.hasShips(Point(x1,y1),Point(xm + 1,ym + 1)):
                        ans += 1
                        if ans >= 10:
                            return ans
                        toA.append((Point(x1,y1),Point(xm + 1,ym + 1)))
                if ym + 1 <= y1:
                    if sea.hasShips(Point(xm,y1),Point(x0,ym + 1)):
                        ans += 1
                        if ans >= 10:
                            return ans
                        toA.append((Point(xm,y1),Point(x0,ym + 1)))
                if xm + 1 <= x1:
                    if sea.hasShips(Point(x1,ym),Point(xm + 1,y0)):
                        ans += 1
                        if ans >= 10:
                            return ans
                        toA.append((Point(x1,ym),Point(xm + 1,y0)))
            fromA = toA
        return ans

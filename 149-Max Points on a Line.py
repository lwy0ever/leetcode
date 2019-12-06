class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # di[(a,b)]表示y = ax + b上的点
        # a等于0时,表示直线y = b
        # a等于float('inf')时,表示直线x = b
        di = {}
        
        def calABC(p1,p2):
            x1 = p1[0]
            y1 = p1[1]
            x2 = p2[0]
            y2 = p2[1]
            if x1 == x2:
                return (float('inf'),x1,1)
            return ((y2 - y1),y1 * (x2 - x1) - (y2 - y1) * x1,x2 - x1)
            
        for i in range(n - 1):
            for j in range(i + 1,n):
                di[(calABC(points[i],points[j]))] = 0
        for i in range(n):
            if (float('inf'),points[i][0],1) in di:
                di[(float('inf'),points[i][0],1)] += 1
            for a,b,c in di:
                if a * points[i][0] + b == points[i][1] * c:
                    di[(a,b,c)] += 1
        #print(di)
        return max(di.values()) if di else len(points)
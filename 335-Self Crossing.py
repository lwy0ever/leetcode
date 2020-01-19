class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        # 当线段条数小于 4 时,不可能发生交叉
        # 线段条数大于等于 4 时,开始出现交叉的可能性:
        #   第 4 条线段只可能与第 1 条线段交叉
        #   第 5 条线段只可能与第 2、1 条线段交叉
        #   第 6 条线段只可能与第 3、(2)、1 条线段交叉
        #   第 7 条线段只可能与第 4、(3)、2 条线段交叉（注意，不可能与第 1 条线段交叉，因为路径是逆时针的，此时线段 1 要么被围在内部，要么被抛在外部）
        #   ...
        n = len(x)
        if n < 4:
            return False
        a,b,c,(d,e,f) = 0,0,0,x[:3]
        for i in range(3,n):
            a,b,c,d,e,f = b,c,d,e,f,x[i]
            if f >= d and e <= c:
                return True
            if e == c and f + b >= d:
                return True
            if d - b <= f <= d and d > b and c - a <= e <= c:
                return True
        return False
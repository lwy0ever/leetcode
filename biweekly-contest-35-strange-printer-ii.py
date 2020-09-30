class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        # 反向考虑,从顶层颜色开始打印,每次的颜色都不覆盖
        m = len(targetGrid)
        n = len(targetGrid[0])
        # 建立一个数据结构(rs,cs,re,ce),表示左上角在(rs,cs),右下角在(re,ce)的矩形
        rect = dict()   # rect[i]表示要覆盖颜色为i的所有单元格,所需要的最小的矩形(rs,cs,re,ce)
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                if c in rect:
                    rect[c] = (min(rect[c][0],i),min(rect[c][1],j),max(rect[c][2],i),max(rect[c][3],j))
                else:
                    rect[c] = (i,j,i,j)
        #print(rect)
        # 逐个单元格考虑
        # 如果该单元格的颜色已经被检查过,则跳过
        # 如果该单元格的颜色c没有被检查过,则做如下检查
        # 1,找到该颜色c形成的矩形
        # 2,检查该矩形内的每个单元格,所有的单元格,要么是颜色c,要么是一种没有被检查过的颜色
        grid = set((i,j) for j in range(n) for i in range(m))
        unchecked = set(rect.keys())
        def gocheck(x,y,unchecked): # 检查点(x,y),未使用的颜色列表在unchecked
            #print(x,y,targetGrid[x][y],unchecked)
            if (x,y) not in grid:
                return True
            c = targetGrid[x][y]
            for i in range(rect[c][0],rect[c][2] + 1):
                for j in range(rect[c][1],rect[c][3] + 1):
                    if (i,j) not in grid:
                        continue
                    if targetGrid[i][j] == c:
                        continue
                    else:
                        if targetGrid[i][j] not in unchecked:
                            return False
                        unchecked.remove(c)
                        if not gocheck(i,j,unchecked):
                            return False
                        unchecked.add(c)
                    grid.remove((i,j))
            return True

        for i in range(m):
            for j in range(n):
                if not gocheck(i,j,unchecked):
                    return False
        return True
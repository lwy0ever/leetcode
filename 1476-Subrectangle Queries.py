class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        # 1 <= rows,cols <= 100,所以最大元素数10000
        # 而updateSubrectangle最多500次,相对是小量
        # 存储updateSubrectangle的history,然后进行查询或许更快一些
        self.rect = rectangle
        self.his = []


    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.his.append((row1,col1,row2,col2,newValue))


    def getValue(self, row: int, col: int) -> int:
        for h in self.his[::-1]:
            if h[0] <= row <= h[2] and h[1] <= col <= h[3]:
                return h[4]
        return self.rect[row][col]



# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
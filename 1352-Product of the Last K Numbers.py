class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.pre = [1]
        self.lastZeroPos = 1

    def add(self, num: int) -> None:
        self.arr.append(num)
        if num == 0:
            self.lastZeroPos = 1
            self.pre.append(1)
        else:
            self.lastZeroPos += 1
            self.pre.append(self.pre[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= self.lastZeroPos:
            return 0
        return self.pre[-1] // self.pre[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.values = [''] * n
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        self.values[id - 1] = value
        ans = []
        if self.ptr == id:
            for i in range(self.ptr - 1,self.n):
                if self.values[i]:
                    ans.append(self.values[i])
                else:
                    break
            self.ptr = i + 1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
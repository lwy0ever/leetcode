class RLEIterator:

    def __init__(self, A: List[int]):
        self.arr = A
        self.cur = 0
        

    def next(self, n: int) -> int:
        while n and self.cur + 1 < len(self.arr):
            #print(n,self.arr,self.cur)
            if self.arr[self.cur] > n:
                self.arr[self.cur] -= n
                return self.arr[self.cur + 1]
            elif self.arr[self.cur] == n:
                self.cur += 2
                return self.arr[self.cur - 1]
            else:
                n -= self.arr[self.cur]
                self.cur += 2
        return -1
      


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
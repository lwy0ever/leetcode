from collections import Counter
class Window:
    def __init__(self):
        self.cnt = Counter()
        self.diff = 0

    def add(self, x):
        self.cnt[x] += 1
        if self.cnt[x] == 1:
            self.diff += 1

    def remove(self, x):
        self.cnt[x] -= 1
        if self.cnt[x] == 0:
            self.diff -= 1

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        w1 = Window()
        w2 = Window()
        left1 = 0
        left2 = 0
        
        ans = 0
        n = len(A)
        for i in range(n):
            x = A[i]
            w1.add(x)
            w2.add(x)

            while w1.diff > K:
                w1.remove(A[left1])
                left1 += 1

            while w2.diff >= K:
                w2.remove(A[left2])
                left2 += 1

            ans += left2 - left1

        return ans

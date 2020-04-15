class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        arr = [x for x in range(n)]
        start = 0
        l = n
        for i in range(n - 1):
            start = (start + m - 1) % l
            arr.pop(start)
            l -= 1
        return arr[0]
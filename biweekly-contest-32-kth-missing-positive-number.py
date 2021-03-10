class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        c = 1
        i = 0
        arr.append(float('inf'))
        while True:
            while c != arr[i] and k > 0:
                c += 1
                k -= 1
            if k == 0:
                return c - 1
            c += 1
            i += 1
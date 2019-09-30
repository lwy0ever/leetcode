class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        s = 0
        cnt = 0
        for a in arr:
            if s + a <= 5000:
                s += a
                cnt += 1
            else:
                break
        return cnt
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        s = sum(arr)
        if s <= target:
            return max(arr)
        n = len(arr)
        arr.sort()
        if arr[0] * n >= target:
            if abs(target // n * n - target) <= abs(int(target / n + 0.5) * n - target):
                return target // n
            else:
                return int(target / n + 0.5)
        ans = 0
        mi = float('inf')
        for i in range(n - 1,0,-1):
            s = s - arr[i]
            t1 = (target - s) // (n - i)
            if t1 >= arr[i - 1]:
                if abs(target - s - t1 * (n - i)) < mi:
                    mi = abs(target - s - t1 * (n - i))
                    ans = t1
            t2 = int((target - s) / (n - i) + 0.5)
            if t2 >= arr[i - 1]:
                if abs(target - s - t2 * (n - i)) < mi:
                    mi = abs(target - s - t2 * (n - i))
                    ans = t2
        return ans
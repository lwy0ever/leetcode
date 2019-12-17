class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        ans = []
        for l in range(len(str(low)),len(str(high)) + 1):
            for i in range(9 - l + 1):
                t = int(s[i:i + l])
                if low <= t <= high:
                    ans.append(t)
        return ans
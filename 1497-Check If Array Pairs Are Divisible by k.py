class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        m = [0] * k
        for a in arr:
            m[a % k] += 1
        for i in range(1,k):
            if m[i] != m[k - i]:
                return False
        return m[0] % 2 == 0
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n <= 2:
            return True
        t = A[0] - A[-1]
        if t == 0:
            for i in range(n - 1):
                if A[i] != A[i + 1]:
                    return False
            return True
        for i in range(n - 1):
            if t * (A[i] - A[i + 1]) < 0:
                return False
        return True
            
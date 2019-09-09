class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        n = len(A)
        if n != len(B):
            return False
        for i in range(n):
            if A[i:] + A[:i] == B:
                return True
        return False
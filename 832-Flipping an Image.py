class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        rn = len(A)
        if rn == 0:
            return A
        cn = len(A[0])
        if cn == 0:
            return A
        for i in range(rn):
            for j in range((cn - 1) // 2 + 1):
                A[i][j],A[i][-j-1] = A[i][-j-1] ^ 1,A[i][j] ^ 1
        return A
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        oddcur = 1
        i = 0
        while i < n:
            if A[i] & 1:    # 奇数
                A[i],A[oddcur] = A[oddcur],A[i]
                oddcur += 2
            else:   # 偶数
                i += 2
        return A
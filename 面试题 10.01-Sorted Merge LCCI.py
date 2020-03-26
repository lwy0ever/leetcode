class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        # 双指针,从尾部开始
        A.insert(0,float('-inf'))   # 前置哨兵
        B.insert(0,float('-inf'))   # 前置哨兵
        i = m
        j = n
        p = m + n
        while p > 0:
            if A[i] >= B[j]:
                A[p] = A[i]
                i -= 1
            else:
                A[p] = B[j]
                j -= 1
            p -= 1
        A.pop(0)
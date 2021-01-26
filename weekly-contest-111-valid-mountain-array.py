class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        if A[0] < A[1]:
            inc = True
        else:
            return False
        pre = A[1]
        for x in A[2:]:
            if x > pre:
                if inc:
                    pre = x
                    continue
                else:
                    return False
            elif x < pre:
                if inc:
                    inc = False
                pre = x
                continue
            else:   # x == pre
                return False
        return not inc
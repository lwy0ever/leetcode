class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sA = sum(A)
        sB = sum(B)
        if sA == sB:
            return [0,0]
        #setA = set(A)
        setB = set(B)
        gap = (sA - sB) // 2
        for a in A:
            if a - gap in setB:
                return [a,a - gap]
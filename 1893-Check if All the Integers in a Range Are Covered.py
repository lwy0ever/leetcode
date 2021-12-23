class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        toCover = set(i for i in range(left,right + 1))
        for s,e in ranges:
            for i in range(s,e + 1):
                toCover.discard(i)
        #print(toCover)
        return len(toCover) == 0
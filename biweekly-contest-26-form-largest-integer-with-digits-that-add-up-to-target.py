class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        def comp(a,b):
            if len(a) > len(b):
                return a
            if len(a) < len(b):
                return b
            return max(a,b)

        preCost = [''] + [None] * target    # preCost[i]表示花费i时,可以组成的最大数,None表示无解
        d = {}  # d[x]表示花费x可以组成的数字
        for i,c in enumerate(cost):
            d[c] = i + 1
        for c in range(1,target + 1):
            for k in d:
                if c - k >= 0:
                    if preCost[c - k] is not None:
                        newStr = str(d[k]) + preCost[c - k]
                        if preCost[c] is None:
                            preCost[c] = newStr
                        else:
                            preCost[c] = comp(newStr,preCost[c])
        return preCost[-1] if preCost[-1] else '0'
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # 一个矩形和另一个矩形取交集,交集的部分是数字最大的
        # 两个矩形的左上角是对齐的,所以只需要看交集的右下角
        maxM,maxN = m,n
        for a,b in ops:
            maxM = min(maxM,a)
            maxN = min(maxN,b)
        return maxM * maxN
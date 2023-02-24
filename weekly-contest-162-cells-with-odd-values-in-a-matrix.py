class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # 方法2:计数优化
        maskM = [0] * m # 记录每行被改变的次数
        maskN = [0] * n # 记录每列被改变的次数
        for r,c in indices:
            maskM[r] ^= 1
            maskN[c] ^= 1
        row = sum(maskM)
        col = sum(maskN)
        return row * (n - col) + col * (m - row)
        
        # 方法1:
        maskM = [0] * m # 记录每行被改变的次数
        maskN = [0] * n # 记录每列被改变的次数
        for r,c in indices:
            maskM[r] += 1
            maskN[c] += 1
        ans = 0
        for r in maskM:
            for c in maskN:
                ans += ((r + c) & 1)
        return ans
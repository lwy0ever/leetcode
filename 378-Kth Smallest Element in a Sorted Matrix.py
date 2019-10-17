class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        cur = [0] * n   # n个指针,记录每行的当前指针位置
        val = []    # 记录当前n个指针指向的值,已排序
        valPos = [] # 记录当前n个指针指向的值所在的行,已按照值排序
        for i in range(n):
            pos = bisect.bisect(val,matrix[i][0])
            valPos.insert(pos,i)
            val.insert(pos,matrix[i][0])
        ans = 0
        for _ in range(k):
            ans = val.pop(0)
            row = valPos.pop(0)
            cur[row] += 1
            if cur[row] < n:
                pos = bisect.bisect(val,matrix[row][cur[row]])
                valPos.insert(pos,row)
                val.insert(pos,matrix[row][cur[row]])
        return ans
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])

        #print(preCal)
        ans = float('-inf')
        # 由于可能n >> m,所以以列为边界
        for left in range(m):
            rowSum = [0] * n
            for right in range(left,m):
                for i in range(n):
                    rowSum[i] += matrix[i][right]
                # rowSum是左边界为left,右边界为right,每行的和
                # 在left，right为边界下的矩阵，求不超过K的最大数值和
                arr = [0]
                addedSum = 0    # 行累加和
                for row in rowSum:
                    addedSum += row
                    # 二分法
                    # 如果查找之前的累加和大于等于addedSum - k的位置
                    # 由于addedSum - k <= arr[loc]
                    # 所以addedSum - arr[loc] <= k
                    loc = bisect.bisect_left(arr,addedSum - k)
                    # 存储可能的结果
                    if loc < len(arr):
                        ans = max(addedSum - arr[loc], ans)
                    # 把累加和加入
                    bisect.insort(arr, addedSum)
        return ans
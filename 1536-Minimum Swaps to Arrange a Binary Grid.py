class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # "主对角线以上的格子全部都是0"也就是右上角都是0
        n = len(grid)
        first1 = [0] * n    # 记录每一行从右往左,第一个1出现的位置
        for i in range(n):
            for j in range(n - 1,-1,-1):
                if grid[i][j] == 1:
                    first1[i] = j
                    break
        # 如果最终满足要求,那么第i行的first1[i] <= i
        # 设i < j,那么first1[i] <= i,first1[j] <= j,可以放置于第i行的,一定可以放置在第j行
        # 也就是说,不会存在第j行占用了本应放置于第i行的情况
        # 所以,在考虑第i行的时候,只需要找到第一个满足i行要求的即可
        ans = 0
        noUsed = [i for i in range(n)]
        for i in range(n):  # 考虑第i行
            for j in range(n - i):  # 剩余n - i行可用
                if first1[noUsed[j]] <= i:   # 第j行可用
                    ans += j    # 上移j行
                    noUsed.pop(j)
                    break
            else:
                return -1
        return ans
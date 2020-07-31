class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # 由于k <= min(200,n ^ m),比较小,可以只查找最小的前k个数字
        # 暴力法
        m = len(mat)
        n = len(mat[0])
        arr = mat[0][:k]    # 只有前k个可能有用
        for i in range(1,m):
            new_arr = []
            for a in arr:
                for j in range(n):
                    new_arr.append(a + mat[i][j])
            new_arr.sort()
            arr = new_arr[:k]   # 只有前k个可能有用
        return arr[-1]
            
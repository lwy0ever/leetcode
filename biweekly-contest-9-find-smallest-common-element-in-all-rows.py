class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        pos = [0] * n
        ans = -1
        ma = -1
        while pos[0] < m:
            i = 1
            while i < n:
                while True:
                    if mat[i][pos[i]] < mat[0][pos[0]]:
                        pos[i] += 1
                    elif mat[i][pos[i]] > mat[0][pos[0]]:
                        pos[0] += 1
                        i = n
                        break
                    else:#==
                        i += 1
                        if i == n:
                            return mat[0][pos[0]]
                        break
        return -1
        
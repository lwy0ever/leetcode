class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s = 0
                cnt = 0
                for x in range(-1,2):
                    for y in range(-1,2):
                        if 0 <= i + x < m and 0 <= j + y < n:
                            s += img[i + x][j + y]
                            cnt += 1
                ans[i][j] = s // cnt
        return ans

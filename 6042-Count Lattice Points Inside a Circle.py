class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = set()
        for x,y,r in circles:
            for i in range(x - r,x + r + 1):
                for j in range(y - r,y + r + 1):
                    if (i,j) in ans:
                        continue
                    if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
                        ans.add((i,j))
        return len(ans)
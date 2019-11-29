class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] * (rowIndex + 1)
        for row in range(rowIndex):
            for i in range(row,0,-1):
                ans[i] += ans[i - 1]
            #print(ans)
        return ans
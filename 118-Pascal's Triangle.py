class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            arr = [1] * (i + 1)
            for j in range(1,i):
                arr[j] = ans[i - 1][j - 1] + ans[i - 1][j]
            ans.append(arr)
            #print(ans)
        return ans
        '''
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(numRows - 1):
            pre = 0
            arr = []
            #print(ans[i])
            for a in ans[i]:
                #print(a)
                arr.append(pre + a)
                pre = a
            arr.append(ans[i][-1])
            #print(arr)
            ans.append(arr)
        return ans
        '''
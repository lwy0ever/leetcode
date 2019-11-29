class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 空间复杂度O(1)
        # 从下向上,利用triangle自身保存数据
        n = len(triangle)
        while n > 1:
            for i in range(n - 1):
                triangle[n - 2][i] += min(triangle[n - 1][i],triangle[n - 1][i + 1])
            n -= 1
        return triangle[0][0]
        # 空间复杂度O(n)
        '''
        n = len(triangle)
        arr = [0] * n
        arr[0] = triangle[0][0]
        for l in range(1,n):
            arr[l] = arr[l - 1] + triangle[l][l]
            for i in range(l - 1,0,-1):
                arr[i] = min(arr[i - 1:i + 1]) + triangle[l][i]
            arr[0] += triangle[l][0]
            #print(arr)
        return min(arr)
        '''
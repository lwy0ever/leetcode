class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        # 从arr[0]开始,最长非递减的结束位置
        i = 0
        while i < n - 1:
            if arr[i] > arr[i + 1]:
                break
            i += 1
        left = i
        if left == n - 1:
            return 0
        # 从arr[n - 1]开始向左,最长非递增的结束位置
        i = n - 1
        while i > 0:
            if arr[i - 1] > arr[i]:
                break
            i -= 1
        right = i
        #print(left,right)
        # 保留左侧or右侧
        ans = min(n - 1 - left,right)
        # 去掉中间一部分
        i = 0
        j = right
        # 尝试去掉[i,j]
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                # 去掉[i,j]后满足要求
                ans = min(ans,j - i - 1)
                # 尝试[i + 1,j]
                i += 1
            else:
                # 由于[i - 1,j]之前已经考虑过了,所以尝试[i,j + 1]
                j += 1
        return ans
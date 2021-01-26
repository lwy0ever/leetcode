class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # 左右指针指向两端点,逐步向中间移动
        ans = []
        n = len(A)
        left = 0
        right = n - 1
        while left <= right:
            if A[left] * A[left] < A[right] * A[right]:
                ans.append(A[right] * A[right])
                right -= 1
            else:
                ans.append(A[left] * A[left])
                left += 1
        return ans[::-1]
        
        # 找到正负数分界点，然后向两侧移动
        '''
        n = len(A)
        negative = -1
        for i in range(n):
            if A[i] < 0:
                negative = i
            else:
                break
        ans = []
        left = negative
        right = negative + 1
        while left >= 0 and right < n:
            if abs(A[left]) < abs(A[right]):
                ans.append(A[left] * A[left])
                left -= 1
            else:
                ans.append(A[right] * A[right])
                right += 1
        while left >= 0:
            ans.append(A[left] * A[left])
            left -= 1
        while right < n:
            ans.append(A[right] * A[right])
            right += 1
        return ans
        '''
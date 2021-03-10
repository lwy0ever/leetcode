class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        ans = K
        left = 0
        right = 0
        length = 0
        used = 0
        while right < n:
            if A[right] == 0:
                used += 1
                while used > K:
                    if A[left] == 0:
                        used -= 1
                    left += 1
            right += 1
            ans = max(ans,right - left)
        return ans
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        ans = []
        remains = 0
        while K:
            K,m = divmod(K,10)
            if A:
                x = A.pop()
            else:
                x = 0
            remains,left = divmod(remains + m + x,10)
            ans.append(left)
        while A:
            remains,left = divmod(remains + A.pop(),10)
            ans.append(left)
        if remains:
            ans.append(remains)
        return ans[::-1]
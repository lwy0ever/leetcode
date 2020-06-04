class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # a == b时,a ^ b == 0
        # 也就是arr[i] ^ arr[i + 1] ^ ... ^ arr[k] == 0
        # j的位置不重要,j可以取i + 1到k,共k - i个值
        ans = 0
        n = len(arr)
        for i in range(n - 1):
            t = arr[i]
            for k in range(i + 1,n):
                t ^= arr[k]
                if t == 0:
                    ans += k - i
        return ans
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        left = []
        right = []
        for i in range(1,int(n ** 0.5) + 1):
            d,m = divmod(n,i)
            if m == 0:
                left.append(i)
                right.append(d)
        if left[-1] == right[-1]:
            right.pop()
        #print(left,right)
        arr = left + right[::-1]
        return arr[k - 1] if len(arr) >= k else - 1
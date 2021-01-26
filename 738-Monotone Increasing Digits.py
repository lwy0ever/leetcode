class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # 从后向前遍历
        # 如果前面的数字大于后面的数字,则前面的数字-1,后面的数字变成9
        arr = list(map(int,list(str(N))))
        l = len(arr)
        pos = -1
        for i in range(l - 2,-1,-1):
            if arr[i] > arr[i + 1]:
                arr[i] -= 1
                pos = i
        #print(pos,arr)
        if pos == -1:
            return N
        else:
            a = 0
            for i in range(pos + 1):
                a = a * 10 + arr[i]
            return a * 10 ** (l - pos - 1) + 10 ** (l - pos - 1) - 1
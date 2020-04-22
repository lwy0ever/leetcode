class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fi = [1,1]
        while fi[-1] < k:
            fi.append(fi[-2] + fi[-1])
        #print(fi)
        ans = 0
        ind = 1
        while k > 0:
            if fi[-ind] <= k:
                k -= fi[-ind]
                ans += 1
            else:
                ind += 1
        return ans
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        m = arr[(n - 1) // 2]
        arr.sort(key = lambda x:(abs(x - m),x))
        return arr[n - k:]
        '''
        narr = []
        for a in arr:
            narr.append((abs(a - m),a))
        narr.sort(key = lambda x:[-x[0],-x[1]])
        ans = []
        for i in range(k):
            ans.append(narr[i][1])
        return ans
        '''
        
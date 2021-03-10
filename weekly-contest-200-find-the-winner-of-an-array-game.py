class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k > n - 1:
            return max(arr)
        _max = arr[0]
        cnt = 0
        ind = 1
        while cnt < k:
            if _max > arr[ind]:
                cnt += 1
            else:
                _max = arr[ind]
                cnt = 1
            ind += 1
            if ind == n:
                ind = 0
        return _max
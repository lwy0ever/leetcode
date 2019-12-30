class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ma = -1
        for i in range(n - 1,-1,-1):
            arr[i],ma = ma,max(ma,arr[i])
        return arr
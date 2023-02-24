class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        aaa = list(set(arr))
        aaa.sort()
        pos = dict()
        for i,a in enumerate(aaa,start = 1):
            pos[a] = i
        for i in range(n):
            arr[i] = pos[arr[i]]
        return arr
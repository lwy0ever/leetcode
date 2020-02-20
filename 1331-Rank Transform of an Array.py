class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = list(set(arr))
        s.sort()
        indexMap = dict(zip(s,range(1,len(s) + 1)))
        for i in range(len(arr)):
            arr[i] = indexMap[arr[i]]
        return arr
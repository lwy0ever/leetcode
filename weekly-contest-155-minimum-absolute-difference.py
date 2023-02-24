class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        mi = float('inf')
        n = len(arr)

        arr.sort()
        for i in range(n - 1):
            t = arr[i + 1] - arr[i]
            if t < mi:
                mi = t
                ans = [[arr[i],arr[i + 1]]]
            elif t == mi:
                ans.append([arr[i],arr[i + 1]])
        return ans
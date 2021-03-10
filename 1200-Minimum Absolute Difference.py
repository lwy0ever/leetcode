class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        mi = float('inf')
        for i in range(n - 1):
            dis = arr[i + 1] - arr[i]
            if dis < mi:
                mi = dis
                ans = [[arr[i],arr[i + 1]]]
            elif dis == mi:
                ans.append([arr[i],arr[i + 1]])
        return ans
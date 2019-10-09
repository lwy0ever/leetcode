class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        p1 = p2 = p3 = 0
        ans = []
        n1 = len(arr1)
        n2 = len(arr2)
        n3 = len(arr3)
        while p1 < n1 and p2 < n2 and p3 < n3:
            ma = max(arr1[p1],arr2[p2],arr3[p3])
            if arr1[p1] == arr2[p2] and arr2[p2] == arr3[p3]:
                ans.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
                continue
            if arr1[p1] < ma:
                p1 += 1
            if arr2[p2] < ma:
                p2 += 1
            if arr3[p3] < ma:
                p3 += 1
        return ans
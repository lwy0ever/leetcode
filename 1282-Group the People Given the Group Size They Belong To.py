class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ug = []
        for u,g in enumerate(groupSizes):
            ug.append((u,g))
        ug.sort(key = lambda x:x[1])
        print(ug)
        ans = []
        oneGroup = []
        for u,g in ug:
            oneGroup.append(u)
            if len(oneGroup) == g:
                ans.append(oneGroup)
                oneGroup = []
        return ans
            
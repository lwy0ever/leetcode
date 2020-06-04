class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        fcs = []
        for l in favoriteCompanies:
            fcs.append(set(l))
        #print(f)
        for i,fc in enumerate(fcs):
            for j,o in enumerate(fcs):
                if i == j:
                    continue
                if fc.issubset(o):
                    break
            else:
                ans.append(i)
        return ans
                
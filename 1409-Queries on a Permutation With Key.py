class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ans = []
        p = [i for i in range(1,m + 1)]
        for q in queries:
            pos = p.index(q)
            t = p.pop(pos)
            p.insert(0,t)
            ans.append(pos)
        return ans
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        # 模拟试试
        arr = [i for i in range(1,m + 1)]
        ans = list()
        for q in queries:
            pos = arr.index(q)
            ans.append(pos)
            arr.pop(pos)
            arr.insert(0,q)
        return ans
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        em = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] == -1:
                continue
            em[manager[i]].append(i)
        #print(em)

        def nom(h,m,it):
            ans = 0
            for e in em[h]:
                ans = max(ans,nom(e,m,it))
            return it[h] + ans
        
        return nom(headID,manager,informTime)
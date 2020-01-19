class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        fromTo = collections.defaultdict(list)
        for f,t in tickets:
            fromTo[f].append(t)
        #print(fromTo)
        for k in fromTo:
            fromTo[k].sort()
        #print(fromTo)
        ans = [''] * (len(tickets) + 1)
        f = 'JFK'
        ans[0] = f
        
        def dfs(f,ind):
            #print(f,ind)
            if ind == len(tickets) + 1:
                return True
            for i,t in enumerate(fromTo[f]):
                ans[ind] = t
                fromTo[f].pop(i)
                if dfs(t,ind + 1):
                    return True
                fromTo[f].insert(i,t)
        
        dfs(f,1)
        return ans
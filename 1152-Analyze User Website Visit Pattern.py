from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        uw = defaultdict(list)
        n = len(username)
        t = sorted(list(enumerate(timestamp)),key = lambda x:x[1])
        #print(t)
        for e in t:
            i = e[0]
            uw[username[i]].append(website[i])
        #print(uw)
        path = defaultdict(int)
        for k in uw.keys():
            for p in set(list(combinations(uw[k],3))):
                path[p] += 1
        #print(path)
        ma = 0
        ans = None
        for k in sorted(path.keys()):
            if path[k] > ma:
                ma = path[k]
                ans = k
        return list(ans)

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # bfs
        if source == target:
            return 0
        ft = collections.defaultdict(set)   # ft[x] = {y1,y2...yn}  表示站点x可以到达线路y1,y2...yn
        for route,sites in enumerate(routes):
            for site in sites:
                ft[site].add(route)
        fromP = set()    # 表示当前所在的线路
        visited = set()  # 表示已经访问过的线路
        for r in ft[source]:
            fromP.add(r)
            visited.add(r)
        ans = 1
        while fromP:
            toP = set()
            for f in fromP:
                for site in routes[f]:
                    if target == site:
                        return ans
                    for route in ft[site]:
                        if route not in visited:
                            toP.add(route)
                            visited.add(route)
            fromP = toP
            ans += 1
        return -1
            
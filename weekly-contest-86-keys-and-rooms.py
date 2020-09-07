class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        # bfs
        fromP = {0}
        visited = {0}
        while fromP:
            toP = set()
            for f in fromP:
                for t in rooms[f]:
                    if t not in visited:
                        visited.add(t)
                        toP.add(t)
            fromP = toP
            #print(fromP)
        return len(visited) == n
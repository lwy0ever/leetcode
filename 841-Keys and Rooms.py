class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        #opened = {0}
        newKey = rooms[0]
        key = {0}
        while newKey:
            #print(newKey)
            newNewKey = []
            for k in newKey:
                key.add(k)
                for nk in rooms[k]:
                    if nk not in key:
                        newNewKey.append(nk)
            newKey = newNewKey
            #print(key,newKey)
        return len(key) == n
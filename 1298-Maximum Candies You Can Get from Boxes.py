class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        ans = 0
        visited = set()
        key = set()
        box = set()
        newBox = set(initialBoxes)
        newKey = set()
        while newBox or newKey:
            box = box.union(newBox)
            #print(box)
            key = key.union(newKey)
            #print(key)

            #print(box,key)
            newnewBox = set()
            newnewKey = set()
            for b in newBox:
                if status[b] == 1 or b in key:
                    ans += candies[b]
                    visited.add(b)
                    #print(visited)
                    for nb in containedBoxes[b]:
                        #print(nb)
                        if nb not in visited:
                            newnewBox.add(nb)
                    #print(newBox)
                    for k in keys[b]:
                        #print(k)
                        if k not in visited:
                            newnewKey.add(k)
                    #print(newKey)
            for b in newKey:
                if b in visited:
                    continue
                if b in box:
                    ans += candies[b]
                    visited.add(b)
                    #print(visited)
                    for nb in containedBoxes[b]:
                        #print(nb)
                        if nb not in visited:
                            newnewBox.add(nb)
                    #print(newBox)
                    for k in keys[b]:
                        #print(k)
                        if k not in visited:
                            newnewKey.add(k)
                    #print(newKey)
            newBox = newnewBox
            newKey = newnewKey
        return ans
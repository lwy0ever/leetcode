class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        ans = 0
        visited = set()
        key = set()
        box = set(initialBoxes)
        while box:
            #print(box,key)
            newBox = set()
            removeBox = set()
            newKey = set()
            for b in box:
                if status[b] == 1 or b in key:
                    ans += candies[b]
                    visited.add(b)
                    #print(visited)
                    for nb in containedBoxes[b]:
                        #print(nb)
                        if nb not in visited:
                            newBox.add(nb)
                    #print(newBox)
                    for k in keys[b]:
                        #print(k)
                        if k not in visited:
                            newKey.add(k)
                    #print(newKey)
                    removeBox.add(b)
                    #print(removeBox)
            if newBox or newKey:
                box.difference_update(removeBox)
                #print(box)
                box = box.union(newBox)
                #print(box)
                key = key.union(newKey)
                #print(key)
            else:
                return ans
        return ans
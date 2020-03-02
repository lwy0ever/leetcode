class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        father = {i:-1 for i in range(n)}
        for i in range(n):
            if leftChild[i] == i:
                return False
            if rightChild[i] == i:
                return False
            if leftChild[i] >= 0:
                if father[leftChild[i]] == -1:
                    father[leftChild[i]] = i
                else:
                    return False
            if rightChild[i] >= 0:
                if father[rightChild[i]] == -1:
                    father[rightChild[i]] = i
                else:
                    return False
        s = 0
        visited = {s}
        while father[s] >= 0:
            s = father[s]
            if s in visited:
                return False
            visited.add(s)
        child = set(i for i in range(n))
        fromP = {s}
        visited = {s}
        while fromP:
            toP = set()
            for f in fromP:
                if leftChild[f] >= 0:
                    if leftChild[f] not in visited:
                        toP.add(leftChild[f])
                        visited.add(leftChild[f])
                    else:
                        return False
                if rightChild[f] >= 0:
                    if rightChild[f] not in visited:
                        toP.add(rightChild[f])
                        visited.add(rightChild[f])
                    else:
                        return False
            fromP = toP
        if len(visited) == n:
            return True
        else:
            return False
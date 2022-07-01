class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        mx = max([e for s,e in flowers])
        changes = collections.defaultdict(int)
        for s,e in flowers:
            changes[s] += 1
            changes[e + 1] -= 1
        cs = sorted(changes.keys())
        pre = 0
        fs = dict()
        for c in cs:
            pre += changes[c]
            fs[c] = pre
        nCs = len(cs)
        maxF = max(cs)
        #print(cs)
        #print(fs)
        n = len(persons)
        personIndex = [i for i in range(n)]
        personIndex.sort(key = lambda x:persons[x])
        #print(personIndex)
        ans = [0] * n
        indexFlower = 0
        pStart = 0
        while pStart < n and cs[indexFlower] > persons[personIndex[pStart]]:
            pStart += 1
        #print(pStart)
        for pi in range(pStart,n):
            if persons[personIndex[pi]] >= maxF:
                break
            if cs[indexFlower] > persons[personIndex[pi]]:
                continue
            while indexFlower + 1 < nCs and persons[personIndex[pi]] >= cs[indexFlower + 1]:
                indexFlower += 1
            #print(pi,persons[personIndex[pi]],indexFlower)
            if indexFlower < nCs:
                ans[personIndex[pi]] = fs[cs[indexFlower]]
        return ans
class Solution:
    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        ans = []
        child = [[] for _ in range(n + 1)]
        fa = [0] * (n + 1)
        coin = [0] * (n + 1)    #coin[i]表示i以及i的下属的总coin
        for f,c in leadership:
            child[f].append(c)
            fa[c] = f
        #print(fa)
        #print(child)
        def addcoin(i,c):
            if i == 0:
                return
            coin[i] += c
            addcoin(fa[i],c)
        
        def childcoin(i,c): #为i及下属增加c个coin,返回自己以及下属增加的coin和
            t = sum([childcoin(j,c) for j in child[i]],0) + c
            coin[i] += t
            return t
        for o in operations:
            if o[0] == 1:
                addcoin(o[1],o[2])
            elif o[0] == 2:
                t = childcoin(o[1],o[2])
                addcoin(fa[o[1]],t)
            else:   #op 3
                ans.append(coin[o[1]] % 1000000007)
            #print(coin)
        return ans
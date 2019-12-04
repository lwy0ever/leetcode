class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        child = collections.defaultdict(list)
        ans = nodes
        for i in range(nodes):
            child[parent[i]].append(i)
        #print(child)
        
        def check(p):
            #print(p)
            #print(p in child)
            nonlocal ans
            if p in child:
                ttl = value[p]
                num = 1
                for c in child[p]:
                    #print(p,c)
                    s,n = check(c)
                    ttl += s
                    num += n
                if ttl == 0:
                    ans -= num
                    return 0,0
                else:
                    return ttl,num
            else:
                if value[p] == 0:
                    ans -= 1
                    return 0,0
                else:
                    return value[p],1
        
        check(0)
        return ans
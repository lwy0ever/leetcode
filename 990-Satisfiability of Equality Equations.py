class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        import copy
        # 满足方程也就意味着所有==的变量,之间没有!=的关系
        base = ord('a')
        eq = [set(chr(base + i)) for i in range(26)]
        noeq = [set() for _ in range(26)]
        for e in equations:
            if e[1] == '=':
                eq[ord(e[0]) - base].add(e[3])
                eq[ord(e[3]) - base].add(e[0])
            else:
                if e[0] == e[3]:
                    return False
                if e[0] < e[3]:
                    noeq[ord(e[0]) - base].add(e[3])
                else:
                    noeq[ord(e[3]) - base].add(e[0])
        #print(eq)
        #print(noeq)
        for i in range(26):
            #print(chr(base + i))
            # bfs
            fromP = eq[i]
            #print(fromP)
            visited = copy.copy(fromP)
            while fromP:
                toP = set()
                for f in fromP:
                    for t in eq[ord(f) - base]:
                        toP.add(t)
                        visited.add(t)
                    eq[ord(f) - base] = set()
                fromP = toP
                #print(fromP)
            eq[i] = visited
        #print(eq)
        for i,ns in enumerate(noeq):
            for n in ns:
                for e in eq:
                    if chr(base + i) in e and n in e:
                        return False
        return True

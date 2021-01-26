class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # tuple比str快
        t = tuple(map(int,s))
        visited = {t}
        fromP = {t}
        while fromP:
            toP = set()
            for s in fromP:
                # 累加
                sa = []
                for i,c in enumerate(s):
                    if i & 1:
                        sa.append((c + a) % 10)
                    else:
                        sa.append(c)
                sa = tuple(sa)
                if sa not in visited:
                    visited.add(sa)
                    toP.add(sa)
                # 轮转
                sb = s[b:] + s[:b]
                if sb not in visited:
                    visited.add(sb)
                    toP.add(sb)

            fromP = toP
            #print(fromP)
            #print(visited)
        return ''.join(map(str,min(visited)))
        '''
        visited = {s}
        fromP = {s}
        while fromP:
            toP = set()
            for s in fromP:
                # 累加
                sa = ''
                for i,c in enumerate(s):
                    if i & 1:
                        sa += str((int(c) + a))[-1]
                    else:
                        sa += c
                if sa not in visited:
                    visited.add(sa)
                    toP.add(sa)
                # 轮转
                sb = s[b:] + s[:b]
                if sb not in visited:
                    visited.add(sb)
                    toP.add(sb)

            fromP = toP
            #print(fromP)
            #print(visited)
        return min(visited)
        '''
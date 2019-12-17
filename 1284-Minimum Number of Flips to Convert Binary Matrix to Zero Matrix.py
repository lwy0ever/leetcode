class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        # bfs
        ans = 0
        m = len(mat)
        n = len(mat[0])
        mt = int('1' * n,2)

        def change(s,i,j):
            ns = s.copy()
            if i - 1 >= 0:
                ns[i - 1] ^= (1 << (n - j - 1))
            t = ((1 << (n - j - 1)) | (1 << (n - j)))
            if n - j - 2 >= 0:
                t |= (1 << (n - j - 2))
            ns[i] ^= t
            ns[i] &= mt
            if i + 1 < m:
                ns[i + 1] ^= (1 << (n - j - 1))
            return ns

        stat = []
        for one in mat:
            stat.append(int(''.join(map(str,one)),2))
        if sum(stat) == 0:
            return 0
        #print(stat)
        visited = set()
        visited.add(str(stat))
        fromS = []
        fromS.append(stat)
        while fromS:
            ans += 1
            #print(ans)
            toS = []
            for s in fromS:
                for i in range(m):
                    for j in range(n):
                        nstat = change(s,i,j)
                        #print(s,nstat)
                        if sum(nstat) == 0:
                            return ans
                        if str(nstat) not in visited:
                            visited.add(str(nstat))
                            toS.append(nstat)
            fromS = toS
        return -1

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        cs = ['A','C','G','T']
        # bfs
        d = set(bank)
        fromP = {start}
        visited = set()
        ans = 0
        while fromP:
            if end in fromP:
                return ans
            toP = set()
            for f in fromP:
                for i in range(8):
                    for c in cs:
                        if f[i] != c:
                            t = f[:i] + c + f[i + 1:]
                            if t in d and t not in visited:
                                toP.add(t)
                                visited.add(t)
            fromP = toP
            ans += 1
        return -1
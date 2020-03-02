class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        d = [[0] * n + [i] for c in votes[0] for i in range(26)]
        base = ord('A')
        for v in votes:
            for i in range(n):
                d[ord(v[i]) - base][i] += 1
        #print(d)
        d.sort(key = lambda x:([-x[i] for i in range(n)] + [x[n]]))
        #print(d)
        ans = ''
        for i in range(n):
            ans += chr(d[i][n] + base)
        return ans
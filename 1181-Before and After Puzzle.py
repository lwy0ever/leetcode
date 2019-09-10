class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        ans = []
        n = len(phrases)
        head = {}
        for i in range(n):
            s = phrases[i].split()
            if s[0] in head:
                head[s[0]].append(i)
            else:
                head[s[0]] = [i]
        for i in range(n):
            s = phrases[i].split()
            if s[-1] in head:
                for j in head[s[-1]]:
                    if i == j:
                        continue
                    ans.append(' '.join(s[:-1] + phrases[j].split()))
        ans = sorted(list(set(ans)))
        return ans
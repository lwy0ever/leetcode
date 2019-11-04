class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        n = len(persons)
        p = persons[0]
        self.ts = [0]    # 记录时间
        self.ps = [p]    # 该时间及该时间之后的获胜者
        d = collections.Counter()  # d[k] 表示k的选票数
        d[p] = 1
        ma = 1
        for i in range(1,n):
            p = persons[i]
            d[p] += 1
            if d[p] >= ma:
                ma = d[p]
                if p != self.ps[-1]:
                    self.ps.append(p)
                    self.ts.append(times[i])
        #print(self.ts)
        #print(self.ps)

    def q(self, t: int) -> int:
        pos = bisect.bisect_right(self.ts,t)
        return self.ps[pos - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
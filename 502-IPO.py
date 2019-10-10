class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        pc = sorted(zip(Profits,Capital),reverse = True)
        #print(pc)
        ans = 0
        for _ in range(k):
            for i,v in enumerate(pc):
                #print(i,v)
                if v[1] <= W:
                    W += v[0]
                    pc.pop(i)
                    break
            else:
                break
        return W
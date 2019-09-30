from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        s = defaultdict(set)  # s[i]是一个set,表示到达stone i前跳跃的距离
        s[1].add(1)
        for st in stones[1:]:
            if st in s:
                for k in s[st]:
                    if k > 1:
                        s[st + k - 1].add(k - 1)
                    s[st + k].add(k)
                    s[st + k + 1].add(k + 1)
        return stones[-1] in s
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        # 其实就是从rounds[0]开始,转若干圈之后到rounds[-1]
        # 如果rounds[0] == rounds[-1],经过最多的就是rounds[0]
        # 如果rounds[0] < rounds[-1],经过最多的就是rounds[0]...rounds[-1]
        # 如果rounds[0] > rounds[-1],经过最多的就是1...rounds[-1]和rounds[0]...n
        if rounds[0] == rounds[-1]:
            return [rounds[0]]
        elif rounds[0] < rounds[-1]:
            return list(range(rounds[0],rounds[-1] + 1))
        else:   # rounds[0] > rounds[-1]
            return list(range(1,rounds[-1] + 1)) + list(range(rounds[0],n + 1))
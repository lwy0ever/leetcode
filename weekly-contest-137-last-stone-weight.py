class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []
        for s in stones:
            heapq.heappush(hp,-s)
        while len(hp) >= 2:
            x = heapq.heappop(hp)
            y = heapq.heappop(hp)
            if x < y:
                heapq.heappush(hp,x - y)
        if hp:
            return -hp[0]
        else:
            return 0
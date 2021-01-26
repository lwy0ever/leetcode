class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        ttl = 0
        cur = 0
        start = 0
        for i in range(n):
            ttl += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0: # 如果从start不能到i站,那么start之间任何一站都不能到i站
                start = i + 1
                cur = 0
        # 如果从start到0是可以完成的,那么会不会从0无法到达start呢?
        # 假设存在0<k<start的k,无法到达,也就是k到start < 0
        # 0到k + k到start + start到0 >=0
        # 所以:0到k + start到0 >= 0,也就是k一定可以到达
        return start if ttl >= 0 else -1
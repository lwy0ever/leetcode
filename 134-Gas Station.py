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
                # 那么从start经过0,一定能到达start吗?
                # 假设存在k(0 < k < start),从start无法到达
                # 0到k + k到start + start到0 >= 0
                # 由于start之前的点都检查过,所以 k到start < 0(否则k就是答案了)
                # 那么 0到k + start到0 > 0,k是可到达的,与假设矛盾
                start = i + 1
                cur = 0
        return start if ttl >= 0 else -1
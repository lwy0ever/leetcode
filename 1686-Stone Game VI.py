class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        # 优先选择自己得分高,对手得分也高的
        n = len(aliceValues)
        sums = [0] * n
        for i in range(n):
            sums[i] = aliceValues[i] + bobValues[i]
        s = list(zip(sums,aliceValues,bobValues))
        s.sort(reverse = True)
        #print(s)
        alice = 0
        bob = 0
        for i in range(n):
            if i & 1:
                bob += s[i][2]
            else:
                alice += s[i][1]
        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        else:
            return 0
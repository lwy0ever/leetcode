class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        ans = 0
        properties.sort(key = lambda x:-x[0])
        #print(properties)
        preAttack = float('inf')
        maxDefence = 0
        maxDefenceTemp = 0
        for a,d in properties:
            if a < preAttack:
                maxDefence = max(maxDefence,maxDefenceTemp)
                maxDefenceTemp = 0
                preAttack = a
            if d < maxDefence:
                ans += 1
            maxDefenceTemp = max(maxDefenceTemp,d)
            #print(a,d,ans)
        return ans
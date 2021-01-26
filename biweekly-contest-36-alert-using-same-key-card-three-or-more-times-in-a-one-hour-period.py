class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        n = len(keyName)
        nameTime = collections.defaultdict(list)
        for i in range(n):
            s = keyTime[i]
            t = s.split(':')
            nameTime[keyName[i]].append(int(t[0]) * 60 + int(t[1]))
        #print(nameTime)
        ans = []
        for k in nameTime.keys():
            nameTime[k].sort()
            m = len(nameTime[k])
            for i in range(2,m):
                if nameTime[k][i] - nameTime[k][i - 2] <= 60:
                    ans.append(k)
                    break
        return sorted(ans)
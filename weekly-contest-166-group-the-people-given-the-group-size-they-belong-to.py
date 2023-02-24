class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        idxCnt = dict() # idxCnt[k] = v,表示当前包含v个人的数组下标.也就是ans[v]
        for i,cnt in enumerate(groupSizes):
            if cnt in idxCnt and len(ans[idxCnt[cnt]]) < cnt:
                ans[idxCnt[cnt]].append(i)
            else:
                idxCnt[cnt] = len(ans)
                ans.append([i])
            #print(ans,idxCnt)
        return ans
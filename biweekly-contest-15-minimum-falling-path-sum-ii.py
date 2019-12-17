class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        m = len(arr[0])
        mi1 = [(100,-1)] * n    # 记录每行最小值及位置
        mi2 = [(100,-1)] * n    # 记录每行次小值及位置
        for i in range(n):
            for j in range(m):
                if arr[i][j] < mi1[i][0]:
                    mi2[i] = mi1[i]
                    mi1[i] = (arr[i][j],j)
                    continue
                elif arr[i][j] < mi2[i][0]:
                    mi2[i] = (arr[i][j],j)
        #print(mi1,mi2)
        ans1 = 0
        pos1 = -1
        ans2 = 0
        pos2 = -1
        for i in range(n):
            #print(ans1,pos1,ans2,pos2)
            #print(mi1[i],mi2[i])
            if pos1 != mi1[i][1]:
                if pos1 != mi2[i][1]:
                    ans2 = ans1 + mi2[i][0]
                    pos2 = mi2[i][1]
                else:
                    ans2 += mi2[i][0]
                    pos2 = mi2[i][1]
                ans1 += mi1[i][0]
                pos1 = mi1[i][1]
            else:
                ans1,ans2 = ans2 + mi1[i][0],ans1 + mi2[i][0]
                pos1 = mi1[i][1]
                pos2 = mi2[i][1]
                if ans1 > ans2:
                    ans1,ans2 = ans2,ans1
                    pos1,pos2 = pos2,pos1
            #print(ans1,pos1,ans2,pos2)
        return ans1
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if T == 0:
            return 0
        # 按照clips[i][0]排序
        clips.sort(key = lambda c:c[0])
        print(clips)
        ans = 0
        ma = 0  # 记录已经经过的起点里最远的结尾
        macur = 0   # 当前起点的最远结尾
        for c in clips:
            if ma >= c[0]: # 可以接上前一段
                if c[0] > macur:    # 如果是新的一段，ans+1，并记录新的结尾
                    ans += 1
                    macur = ma
            else:   # 接不上
                return -1
            if c[1] > ma:   # 有更远的结尾
                ma = c[1]
            if ma >= T: # 可以满足要求T
                break
            #print(c,macur,ma,ans)
        else:   # 循环正常结束，说明没有满足要求T
            return -1
        return ans + 1  # 循环非正常结束，说明T被满足了

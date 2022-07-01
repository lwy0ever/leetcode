class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # 方法2:
        # 纯滑动窗口
        def maxChange(char):    # 改变为char可以获得的最大困扰度
            ans,l,cnt = 0,0,0
            for r in range(len(answerKey)):
                if answerKey[r] != char:
                    cnt += 1
                while cnt > k:
                    if answerKey[l] != char:
                        cnt -= 1
                    l += 1
                ans = max(ans,r - l + 1)
            return ans
        return max(maxChange('T'),maxChange('F'))

        # 方法1:
        # 滑动窗口 + 前缀和
        n = len(answerKey)
        ans = 0
        preT = [0]
        preF = [0]
        for i in range(n):
            if answerKey[i] == 'T':
                preT.append(preT[-1] + 1)
                preF.append(preF[-1])
            else:
                preT.append(preT[-1])
                preF.append(preF[-1] + 1)
        #print(preT)
        #print(preF)
        # T变F
        l = 0
        r = k
        while r <= n:
            if preT[r] - preT[l] > k:
                while preT[r] - preT[l] > k:
                    l += 1
                    #print(l,r)
            else:
                ans = max(ans,r - l)
            r += 1
            #print(ans)
        # F变T
        l = 0
        r = k
        while r <= n:
            if preF[r] - preF[l] > k:
                while preF[r] - preF[l] > k:
                    l += 1
            else:
                ans = max(ans,r - l)
            r += 1
        return ans
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 用ans存放遇到的letter
        # 如果letter < ans[-1],并且以后ans[-1]还会出现,则把ans[-1]弹出,从而保证结果最小
        n = len(s)
        lastPos = [0] * 26
        for i in range(n):
            lastPos[ord(s[i]) - ord('a')] = i
        used = [False] * 26
        ans = ['0'] # 存放一个比'a'小的元素,方便比较,而且永远不会被弹出
        for i in range(n):
            # 之前已有该字母出现,则跳过
            if used[ord(s[i]) - ord('a')]:
                continue
            # 如果s[i] < ans[-1],并且以后ans[-1]还会出现,则把ans[-1]弹出
            while s[i] < ans[-1] and lastPos[ord(ans[-1]) - ord('a')] >= i:
                t = ans.pop()
                used[ord(t) - ord('a')] = False
            ans.append(s[i])
            used[ord(s[i]) - ord('a')] = True
        return ''.join(ans[1:])
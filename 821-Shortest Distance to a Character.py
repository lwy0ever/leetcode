class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        pos = []
        pos.append(float('-inf'))
        for i in range(n):
            if s[i] == c:
                pos.append(i)
        pos.append(float('inf'))
        cnt = len(pos)
        #print(pos)
        ans = []
        pre = float('-inf')
        ind = 0
        for i in range(n):
            if i > pos[ind]:
                pre = pos[ind]
                ind += 1
            ans.append(min(abs(pos[ind] - i),abs(pre - i)))
        return ans
        '''
        # pos[0]左侧是一个递减序列
        # pos[i]和pos[i + 1]之间是一个驼峰
        # pos[-1]右侧是一个递增序列
        ans = 0
        ans += (pos[0] + 1) * pos[0] // 2
        for i in range(cnt - 1):
            l = pos[i + 1] - pos[i]
            if l & 1:   # 位置差是奇数,中间项有偶数个
                ans += (1 + (l - 1) // 2) * (l - 1) // 2
            else:   # 位置差是偶数,中间项有奇数个
                ans += (1 + l // 2) * l // 2 - l // 2
        ans += (n - pos[-1] - 1) * (n - pos[-1]) // 2
        return ans
        '''
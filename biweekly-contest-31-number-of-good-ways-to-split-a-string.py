class Solution:
    def numSplits(self, s: str) -> int:
        # 由于只有小写字母,用数组记录即可
        size = 26
        left = [0] * 26
        right = [0] * 26
        base = ord('a')
        validLeft = 0   # 左边不同的字符数
        validRight = 0  # 右边不同的字符数
        for c in s:
            ind = ord(c) - base
            right[ind] += 1
            if right[ind] == 1:
                validRight += 1
        ans = 0
        for c in s:
            ind = ord(c) - base
            left[ind] += 1
            if left[ind] == 1:
                validLeft += 1
            right[ind] -= 1
            if right[ind] == 0:
                validRight -= 1
            if validLeft == validRight:
                ans += 1
        return ans

        '''
        ans = 0
        cnt1 = collections.Counter()
        cnt2 = collections.Counter(s)
        for c in s:
            cnt1[c] += 1
            cnt2[c] -= 1
            if len(+cnt1) == len(+cnt2):
                ans += 1
        return ans
        '''
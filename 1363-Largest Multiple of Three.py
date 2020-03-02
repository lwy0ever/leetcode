class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        cnt = collections.Counter(digits)
        s = sum(digits)
        m = s % 3
        if m == 1:
            if cnt[1] > 0:
                cnt[1] -= 1
            elif cnt[4] > 0:
                cnt[4] -= 1
            elif cnt[7] > 0:
                cnt[7] -= 1
            elif cnt[2] > 1:
                cnt[2] -= 2
            elif cnt[2] > 0 and cnt[5] > 0:
                cnt[2] -= 1
                cnt[5] -= 1
            elif cnt[5] > 1:
                cnt[5] -= 2
            elif cnt[2] > 0 and cnt[8] > 0:
                cnt[2] -= 1
                cnt[8] -= 1
            elif cnt[5] > 0 and cnt[8] > 0:
                cnt[5] -= 1
                cnt[8] -= 1
            elif cnt[8] > 1:
                cnt[8] -= 2
            else:
                return ''
        elif m == 2:
            if cnt[2] > 0:
                cnt[2] -= 1
            elif cnt[5] > 0:
                cnt[5] -= 1
            elif cnt[8] > 0:
                cnt[8] -= 1
            elif cnt[1] > 1:
                cnt[1] -= 2
            elif cnt[1] > 0 and cnt[4] > 0:
                cnt[1] -= 1
                cnt[4] -= 1
            elif cnt[4] > 1:
                cnt[4] -= 2
            elif cnt[1] > 0 and cnt[7] > 0:
                cnt[1] -= 1
                cnt[7] -= 1
            elif cnt[4] > 0 and cnt[7] > 0:
                cnt[4] -= 1
                cnt[7] -= 1
            elif cnt[7] > 1:
                cnt[7] -= 2
            else:
                return ''
        digits = sorted(cnt.elements(),reverse = True)
        if digits:
            if digits[0] == 0:
                return '0'
            else:
                return ''.join(map(str,digits))
        else:
            return ''
                
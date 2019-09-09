class Solution:
    def intToRoman(self, num: int) -> str:
        lookup = {
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'
        }
        ans = ''
        for key in sorted(lookup.keys(),reverse = True):
            n = num // key
            #if n == 0:
            #    continue
            ans += (lookup[key] * n)
            num -= n * key
            #if num == 0:
            #    break
        return ans
        '''
        nnnn = num // 1000
        nnn = (num % 1000) // 100
        nn = (num % 100) // 10
        n = num % 10
        ans = ''
        ans += 'M' * nnnn
        if nnn == 9:
            ans += 'CM'
        elif nnn <= 8 and nnn >= 5:
            ans += 'D' + 'C' * (nnn - 5)
        elif nnn == 4:
            ans += 'CD'
        elif nnn >= 1:
            ans += 'C' * nnn
        if nn == 9:
            ans += 'XC'
        elif nn <= 8 and nn >= 5:
            ans += 'L' + 'X' * (nn - 5)
        elif nn == 4:
            ans += 'XL'
        elif nn >= 1:
            ans += 'X' * nn
        if n == 9:
            ans += 'IX'
        elif n <= 8 and n >= 5:
            ans += 'V' + 'I' * (n - 5)
        elif n == 4:
            ans += 'IV'
        elif n >= 1:
            ans += 'I' * n
        return ans
        '''        
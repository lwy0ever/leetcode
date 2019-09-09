class Solution:
    def romanToInt(self, s: str) -> int:
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
        length = len(s)
        ans = 0
        pos = 0
        for k in sorted(lookup.keys(),reverse = True):
            n = len(lookup[k])
            while pos + n <= length and s[pos:pos + n] == lookup[k]:
                ans += k
                pos += n
        return ans        
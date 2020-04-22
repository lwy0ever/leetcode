class Solution:
    def reformat(self, s: str) -> str:
        d = {'0','1','2','3','4','5','6','7','8','9'}
        ans = ''
        stackDigital = []
        stackAlphabet = []
        for c in s:
            if c in d:
                stackDigital.append(c)
            else:
                stackAlphabet.append(c)
        if abs(len(stackDigital) - len(stackAlphabet)) <= 1:
            ans = ''
            if len(stackDigital) < len(stackAlphabet):
                for i,d in enumerate(stackDigital):
                    ans += stackAlphabet[i]
                    ans += d
                ans += stackAlphabet[-1]
            elif len(stackDigital) > len(stackAlphabet):
                for i,d in enumerate(stackAlphabet):
                    ans += stackDigital[i]
                    ans += d
                ans += stackDigital[-1]
            else:
                for i,d in enumerate(stackAlphabet):
                    ans += stackDigital[i]
                    ans += d
            return ans
        else:
            return ''
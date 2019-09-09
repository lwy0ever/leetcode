class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'}
        ans = []
        n = len(digits)
        if n == 0:
            return ans
        t = [''] * n
        def trans(digits,i,n,t):
            nonlocal dic
            for c in dic[digits[i]]:
                t[i] = c
                if i < n - 1:
                    trans(digits,i + 1,n,t)
                else:
                    nonlocal ans
                    ans.append(''.join(t))
        trans(digits,0,n,t)
        return ans
            
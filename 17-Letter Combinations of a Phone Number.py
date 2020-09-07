class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
            }
        ans = []
        def dfs(digit,res):
            if digit == '':
                if res:
                    ans.append(res)
                return
            for c in d[digit[0]]:
                dfs(digit[1:],res + c)
            return
        
        dfs(digits,'')
        return ans
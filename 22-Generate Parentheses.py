class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(s,needed,left,right):
            if needed == left:
                if needed == right:
                    ans.append(s)
                else:
                    helper(s + ')',needed,left,right + 1)
            elif needed > left:
                helper(s + '(',needed,left + 1,right)
                if left > right:
                    helper(s + ')',needed,left,right + 1)

        ans = []
        helper('',n,0,0)
        return ans
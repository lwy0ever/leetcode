class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def gP(s,l,r,n):
            if l == n and r == l:
                ans.append(s)
                return
            if l < n:
                gP(s + '(',l + 1,r,n)
            if r < l:
                gP(s + ')',l,r + 1,n)

        gP('(',1,0,n)
        return ans        
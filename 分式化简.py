class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        l = cont.pop()
        ans = [l,1]
        while cont:
            l = cont.pop()
            ans = [ans[0] * l + ans[1],ans[0]]

        def lcd(x,y):
            d,m = divmod(x,y)
            if m == 0:
                return y
            return lcd(y,m)
        
        l = lcd(ans[0],ans[1])
        ans[0] //= l
        ans[1] //= l
        return ans
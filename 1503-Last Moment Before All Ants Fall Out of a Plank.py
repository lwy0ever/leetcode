class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # 两只蚂蚁碰撞,本质上可以理解为两只蚂蚁相互穿过
        ans = 0
        if left:
            ans = max(max(left),ans)
        if right:
            ans = max(n - min(right),ans)
        return ans
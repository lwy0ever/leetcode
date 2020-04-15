class Solution:
    def numOfWays(self, n: int) -> int:
        # 上方的3个格子有如下2大类状态
        # ABC(ACB,BAC,BCA,CAB,CBA),ABA(ACA,BAB,BCB,CAC,CBC)
        # 如果是ABC型,则下方可以是BAB,BCB,BCA,CAB,也就是2个ABC型,2个ABA型
        # 如果是ABA型,则下方可以是BAB,BAC,BCB,CAC,CAB,也就是2个ABC型,3个ABA型
        ABC = 6
        ABA = 6
        for i in range(n - 1):
            ABC,ABA = ABC * 2 + ABA * 2,ABC * 2 + ABA * 3
        return (ABC + ABA) % (10 ** 9 + 7)
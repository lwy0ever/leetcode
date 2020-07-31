class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        def move(m,A,B,C):  # 需要从A移动m个盘子到C,可以借助B
            if m == 1:  # 一个盘子,直接移动
                C.append(A.pop())
                return
            else:
                move(m - 1,A,C,B)   # 先把A上面的m - 1个移动到B上
                C.append(A.pop())   # 把A目前最上面的一个移动到C
                move(m - 1,B,A,C)   # 把B上面的m - 1个移动到C上
        n = len(A)
        move(n,A,B,C)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[': # 纯数字
            return NestedInteger(int(s))
        stack = []
        # num为数字,sign为符号位(1正-1负),is_num表示前一个是否为数字(感觉主要是为了处理[])
        num, sign, is_num = 0, 1, False
        
        for c in s:
            if c == '-':
                sign = -1
            elif c.isdigit():
                num = num * 10 + int(c)
                is_num = True
            elif c == '[':
                stack.append(NestedInteger())   # 加一个空列表
            elif c in (',',']'):
                # 把刚才的数字append进去
                if is_num:
                    stack[-1].add(NestedInteger(sign * num))
                num, sign, is_num = 0, 1, False # 初始化
                # 此时为嵌套列表
                if c == ']' and len(stack) > 1:
                    cur_list = stack.pop()
                    stack[-1].add(cur_list)
        return stack[0]
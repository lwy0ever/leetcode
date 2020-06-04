# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # 二分查找
        # 先二分查找,找到山峰
        # 然后先在左边二分查找
        # 如果没有找到,再在右边二分查找
        # 注意:左右二分查找的时候,功能类似,写成一个函数
        def bs(mountain,target,l,r,key = lambda x:x):
            target = key(target)
            while l <= r:
                m = (l + r) // 2
                cur = key(mountain.get(m))
                if cur == target:
                    return m
                elif cur < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        
        n = mountain_arr.length()
        l = 0
        r = n - 1
        while l < r:
            m = (l + r) // 2
            if mountain_arr.get(m) < mountain_arr.get(m + 1):   # 在山峰左侧
                l = m + 1
            else:
                r = m
        ans = bs(mountain_arr,target,0,m,lambda x:x)
        if ans != -1:
            return ans
        ans = bs(mountain_arr,target,m + 1,n - 1,lambda x:-x)
        return ans
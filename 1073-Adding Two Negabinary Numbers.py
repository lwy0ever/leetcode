class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # arr in base -2
        # means:
        # arr[-1] stand for 1
        # arr[-2] stand for -2
        # arr[-3] stand for 4
        # arr[-4] stand for -8
        # 也就是低位数相加之后,如果产生进位,则 高位数-低位数//2,如果为1或者0,则ok,如果是-1,则继续进位
        ans = []
        n1 = len(arr1)
        n2 = len(arr2)
        i = n1
        j = n2
        jinwei = 0
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            jinwei,s = divmod(arr1[i] + arr2[j] - jinwei,2)
            ans.insert(0,s)
        while i > 0:
            i -= 1
            jinwei,s = divmod(arr1[i] - jinwei,2)
            ans.insert(0,s)
        while j > 0:
            j -= 1
            jinwei,s = divmod(arr2[j] - jinwei,2)
            ans.insert(0,s)
        while jinwei != 0:
            jinwei,s = divmod(- jinwei,2)
            ans.insert(0,s)
        while ans[0] == 0 and len(ans) > 1:
            ans.pop(0)
        return ans
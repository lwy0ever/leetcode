class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 如果数组中全是非负数,则最大的三个数相乘即为最大乘积
        # 如果全是非正数,则最大的三个数相乘同样也为最大乘积
        # 如果数组中有正数有负数,则最大乘积既可能是三个最大正数的乘积,也可能是两个最小负数(即绝对值最大)与最大正数的乘积
        
        # 如上,只需要关心最大的3个数和最小的2个数
        min1 = float('inf')
        min2 = float('inf')
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')
        for n in nums:
            if n > max1:
                max3,max2,max1 = max2,max1,n
            elif n > max2:
                max3,max2 = max2,n
            elif n > max3:
                max3 = n
            if n < min1:
                min2,min1 = min1,n
            elif n < min2:
                min2 = n
        return max(max1 * max2 * max3,max1 * min1 * min2)
            
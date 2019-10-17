class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        ans = 0
        n = len(row)
        # 遍历座位的前一个
        for i in range(0,n,2):
            # row[i] ^ 1为row[i]的配偶的编号
            # 如果row[i + 1]不是row[i]的配偶
            if row[i] ^ 1 != row[i + 1]:
                # 从后面找row[i]的配偶,并交换到i + 1的位置
                for j in range(i + 2,n):
                    if row[i] ^ 1 == row[j]:
                        row[i + 1],row[j] = row[j],row[i + 1]
                        ans += 1
        return ans
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        # ans[i]为考虑到前i个数时的最大和
        ans = [0,A[0]]
        # 从A[1]开始
        n = len(A)
        for i in range(1,n):
            now_max = A[i]  # 将最后一个数独立划分时它即最大值
            ans_max = ans[-1] + A[i]    # 记录目前的最大和，初始为之前数的最大和加独立划分的该数
            for j in range(1,min(i + 1,K)): # 遍历将当前数与前1个数到前K-1个数一起划分，注意不能超过已考虑数的个数
                now_max = max(now_max,A[i - j]) # 更新当前划分的最大值
                ans_max = max(ans_max,ans[- j - 1] + now_max * (j + 1)) # 更新最大和
            ans.append(ans_max) # 记录最大和
        return ans[-1]  # 遍历完成后最后一个值即结果

        
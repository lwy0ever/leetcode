class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # 统计每个数字出现的次数
        cnt = collections.Counter(nums)
        # 记录当前已有的(长度为3及以上)的子序列的结尾值的个数
        endCnt = collections.Counter()
        
        for n in nums:
            if cnt[n] > 0:  # 还有没被考虑的n
                # 优先放在已有的子序列的结尾
                if (preEndCnt := endCnt.get(n - 1,0)) > 0:
                    cnt[n] -= 1
                    endCnt[n - 1] = preEndCnt - 1
                    endCnt[n] += 1
                # 需要新建子序列
                else:
                    # 检查n + 1,n + 2是否存在
                    if (cnt1 := cnt.get(n + 1,0)) > 0 and (cnt2 := cnt.get(n + 2,0)) > 0:
                        cnt[n] -= 1
                        cnt[n + 1] -= 1
                        cnt[n + 2] -= 1
                        endCnt[n + 2] += 1
                    else:
                        return False
        return True
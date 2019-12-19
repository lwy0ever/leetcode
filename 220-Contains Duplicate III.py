class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 利用篮子(桶)
        if t < 0 or k < 0:
            return False
        bucket = {}#篮子bucket[i]存放[size * i,size * i + size - 1]范围内的元素,差最大为size - 1
        size = t + 1 #篮子的大小
        n = len(nums)
        for i in range(n):
            v = nums[i]
            pos = v // size
            if pos in bucket:
                return True
            bucket[pos] = v
            if pos - 1 in bucket and v - bucket[pos - 1] <= t:
                return True
            if pos + 1 in bucket and bucket[pos + 1] - v <= t:
                return True
            if i >= k: # 删除旧篮子
                bucket.pop(nums[i - k] // size)
        return False
        '''
        # 用val存放出现过的值
        # 控制val的长度,val最长为k
        # 长度大于k,则删除当前位置-k的位置的值
        if t < 0:
            return False
        val = set()
        n = len(nums)
        for i in range(n):
            if t == 0:
                if nums[i] in val:
                    return True
            else:
                for oldval in val:
                    if abs(nums[i] - oldval) <= t:
                        return True
            val.add(nums[i])
            if len(val) > k:
                val.remove(nums[i - k])
        return False
        '''
        '''
        # val和pos表示val[i]最后出现在pos[i]处
        val = []
        pos = []
        n = len(nums)
        for i in range(n):
            left = bisect.bisect_left(val,nums[i] - t)
            right = bisect.bisect_right(val,nums[i] + t)
            if right > left:
                for p in pos[left:right]:
                    if i - p <= k:
                        return True
            p = bisect.bisect(val,nums[i])
            if p and val[p - 1] == nums[i]: # nums[i]出现过
                pos[p - 1] = i
            else:
                val.insert(p,nums[i])
                pos.insert(p,i)
            # 将位置在i - k的元素去掉,尽可能缩短val和pos的长度
            if i - k >= 0:
                oldPos = bisect.bisect(pos,i - k)
                if oldPos and pos[oldPos - 1] == i - k:
                    val.pop(oldPos - 1)
                    pos.pop(oldPos - 1)
            #print(val)
            #print(pos)
        return False
        '''
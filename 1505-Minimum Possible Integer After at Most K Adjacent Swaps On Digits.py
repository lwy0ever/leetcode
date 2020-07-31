class Solution:
    def minInteger(self, num: str, k: int) -> str:
        length = len(num)
        kv = [[] for _ in range(10)]
        cur = [0] * 10  # cur[i]存储kv[i]当前可选的位置
        offset = [0] * 10  # offset[i]存储kv[i]中cur[i]位置的偏移,右移为正
        history = [0] * length  # num中对应的数字是否前移，前移(-1)，未前移(0)
        ans = []
        for i, n in enumerate(num):
            kv[int(n)].append(i)
        # 计算最多移动次数
        _max = 0
        for i in range(10):
            for j in range(i + 1,10):
                _max += len(kv[j]) * len(kv[i])
        #print(_max)
        # 如果k >= 最多移动次数,直接排序即可
        if k >= _max:
            return ''.join(sorted(num))
        #print(kv)
        ind = 0 # 当前考虑的第ind位
        #print(ind,ans,k,cur,offset,history)
        while k and ind < length:
            # 从0开始找可以前移的数字
            for i in range(10):
                if cur[i] < len(kv[i]) and kv[i][cur[i]] + offset[i] - ind <= k:  # 符合前移条件
                    k -= kv[i][cur[i]] + offset[i] - ind  # k减去消耗的前移步数
                    #print(kv[i][cur[i]],offset[i],ind,k)
                    ans.append(str(i))
                    ind += 1
                    history[kv[i][cur[i]]] -= 1  # 标记前移的数字

                    # 0-9每个数字更新由于本次前移造成的偏移
                    for j in range(10):
                        if cur[j] < len(kv[j]) and kv[i][cur[i]] >= kv[j][cur[j]]:
                            offset[j] += 1

                    cur[i] += 1  # 当前数字的下一个可前移位置的索引
                    # 更新当前数字的偏移(每遇到一个已经前移的数字，偏移减1)
                    if cur[i] < len(kv[i]):
                        for j in range(kv[i][cur[i] - 1], kv[i][cur[i]]):
                            offset[i] += history[j]

                    break
            #print(ind,ans,k,cur,offset,history)
        # 添加所有未前移的数字
        for i in range(length):
            if history[i] == 0:
                ans.append(num[i])
        return ''.join(ans)
        '''
        # 第1位,需要在n1位之内(n1 <= k),找到最小值
        # 第2位,需要在n2位之内(n2 <= k - n1),找到最小值
        # ...
        length = len(num)
        kv = [[] for _ in range(10)]
        cur = [0] * 10  # cur[i]存储kv[i]当前可选的位置
        for i,n in enumerate(num):
            kv[int(n)].append(i)
        # 计算最多移动次数
        _max = 0
        for i in range(10):
            for j in range(i + 1,10):
                _max += len(kv[j]) * len(kv[i])
        #print(_max)
        # 如果k >= 最多移动次数,直接排序即可
        if k >= _max:
            return ''.join(sorted(num))
        arr = [] # 记录当前每个位置的元素
        for n in num:
            arr.append(n)
        ans = []
        ind = 0
        #print(k,ind,ans,kv)
        # 在k的限制内,找到最小值
        while k > 0 and ind < length:
            for i in range(10):
                if cur[i] < len(kv[i]) and kv[i][cur[i]] - ind <= k:
                    fromPos = kv[i][cur[i]] # 由于将该位置的元素移动到ind的位置,因此从ind到fromPos之前的元素,都要后移1位
                    ans.append(i)
                    k -= (kv[i][cur[i]] - ind)
                    cur[i] += 1
                    ind += 1
                    break
            arr[ind:fromPos + 1] = arr[ind - 1:fromPos]
            for i in range(10): # 将fromPos前面的元素后移
                p = cur[i]
                while p < len(kv[i]):
                    if kv[i][p] < fromPos:
                        kv[i][p] += 1
                    else:
                        break
                    p += 1
            #print(k,ind,ans,kv)
        #print(k)
        # k已经等于0,将剩余元素按照顺序补进去
        ans += arr[ind:]
        return ''.join(map(str,ans))
        '''
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        n = len(num)
        arr = list(map(int,num))
        # 由于"子字符串"是连续序列,需要记录替换的状态
        # 0表示没有替换过,1表示替换过,2表示替换结束
        status = 0
        i = 0
        while i < n and status < 2:
            if change[arr[i]] > arr[i]:
                # 无论status是0还是1,都变成1
                arr[i] = change[arr[i]]
                status = 1
            elif change[arr[i]] < arr[i]:
                # 如果status == 0,不用忽略
                # 如果status == 1,需要结束
                if status == 1:
                    status = 2
            else:   # change[arr[i]] == arr[i]
                # 保持status不变
                pass
            i += 1
        return ''.join(map(str,arr))
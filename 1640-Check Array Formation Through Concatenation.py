class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # 注意arr[i]互不相同
        # 所以任意一个arr[i],都是唯一的
        pos = dict()
        for i,p in enumerate(pieces):
            pos[p[0]] = i
        #used = set()    # 由于arr[i]互不相同,所以used其实没有用处
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] in pos:   # 有以arr[i]为起始的pieces
                #if pos[arr[i]] not in used: # 没有被使用
                l = len(pieces[pos[arr[i]]])    # 这个pieces的长度
                if arr[i:i + l] == pieces[pos[arr[i]]]: # arr接下来的几个字符和这个pieces一致：
                    #used.add(pos[arr[i]])
                    i += l
                    continue
            return False    # 任何一个不满足,则返回False
        return True
            
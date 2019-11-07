class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Func: 计算偏移表
        def calShiftMat(st):
            dic = {}
            for i in range(len(st) - 1,-1,-1):
                if st[i] not in dic:
                    dic[st[i]] = len(st) - i
            dic['ot'] = len(st) + 1
            return dic
        
        # 其他情况判断
        nLen = len(needle)
        hLen = len(haystack)
        if nLen > hLen:
            return -1
        if needle == '':
            return 0
        
        # 偏移表预处理    
        dic = calShiftMat(needle)
        idx = 0
    
        while idx + nLen <= hLen:
            # 待匹配字符串
            str_cut = haystack[idx:idx + nLen]
            
            # 判断是否匹配
            if str_cut == needle:
                return idx
            else:
                # 边界处理
                if idx + nLen >= hLen:
                    return -1
                # 不匹配情况下，根据下一个字符的偏移，移动idx
                cur_c = haystack[idx + nLen]
                if cur_c in dic:
                    idx += dic[cur_c]
                else:
                    idx += dic["ot"]

        return -1 if idx + nLen >= hLen else idx

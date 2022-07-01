class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 计算每个字符的后置字符量,前置字符量
        # 如果一个字符,没有前置字符,则可以认为它最小
        # 然后将这个字符从它的后置字符中去掉

        # 根据已知的w1 < w2,返回可以判定的字符顺序
        # 如果无可以判定的顺序,则返回 False
        def alphabetOrder(w1,w2):
            for c1,c2 in zip(w1,w2):
                if c1 != c2:
                    return c1,c2
            # 两者前len(words[i + 1])个字符相同,words[i]却比words[i + 1]长
            if len(w1) > len(w2):
                return False
            else:
                return True
        
        n = len(words)
        alphabet = set(''.join(words))
        od = collections.defaultdict(set)  # 正序
        rod = collections.defaultdict(set) # 逆序
        for i in range(n - 1):
            if words[i] == words[i + 1]:
                continue
            r = alphabetOrder(words[i],words[i + 1])
            if r == False:
                return ''
            elif r == True:
                continue
            c1,c2 = r
            od[c1].add(c2)
            rod[c2].add(c1)
        inCnt = dict()  # 入度
        for c in alphabet:
            if c in rod:
                inCnt[c] = len(rod[c])
            else:
                inCnt[c] = 0
        #print(od,rod,inCnt)

        ans = []
        while alphabet:
            for c in alphabet:
                #print(c)
                if inCnt[c] == 0:
                    for c2 in od[c]:
                        inCnt[c2] -= 1
                    ans.append(c)
                    del inCnt[c]
                    break
            else:   # 没有找到入度为0的字母,有环
                return ''
            alphabet.discard(ans[-1])
        return ''.join(ans)
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # 方法1:字典树
        '''
        tree = dict()
        for w in words:
            if w:   # 当w == ''时,cur['#'] = None相当于tree['#'] = None,会无限匹配
                cur = tree
                for c in w:
                    cur = cur.setdefault(c,dict())
                cur['#'] = None  # 设置#为结束位标志
        #print(tree)
        
        # 从cur中查找word[pos],已经有cnt个完整的单词被找到
        def dfs(word,pos,cnt,cur):
            #print(word,pos,cnt,cur.keys())
            if pos == len(word):    # word的字符全部找到
                if cnt > 0 and '#' in cur:  # cnt > 0说明找到的不是word自身,# in cur说明是单词结尾
                    return True
                return False
            if '#' in cur:  # 一个单词结尾
                if dfs(word,pos,cnt + 1,tree): # 从tree的开头再找
                    return True
            if word[pos] in cur:
                if dfs(word,pos + 1,cnt,cur[word[pos]]):
                    return True
            return False
        
        ans = []
        for word in words:
            if dfs(word,0,0,tree):
                ans.append(word)
        return ans
        '''

        # 方法2:哈希
        words.sort(key = len)   # 字符串只能由比它更短的字符串组成,所以按长度排序
        #print(words)
        lenSet = set()
        lens = []
        pre = set()
        
        def check(word):
            if word in pre:
                return True
            for l in lens:
                if word[:l] in pre:
                    if check(word[l:]):
                        return True
            return False
        
        ans = []
        for w in words:
            #print(pre,lens,w)
            if not w:   # 处理w == ''时无限循环的问题
                continue
            if check(w):
                ans.append(w)
            pre.add(w)
            l = len(w)
            if l not in lenSet:
                lenSet.add(l)
                lens.append(l)
        return ans
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
        '''
        words.sort(key = len)   # 字符串只能由比它更短的字符串组成,所以按长度排序
        #print(words)
        lens = []
        pre = dict()
        
        def check(word):
            #print(word,lens,pre)
            if not word:
                return True
            if word in pre:
                return pre[word]
            for l in lens:
                if len(word) < l:
                    break
                #print(l,word[:l],word[l:])
                if word[:l] in pre and pre[word[:l]]:
                    pre[word[l:]] = check(word[l:])
                    if pre[word[l:]]:
                        return True
            pre[word] = False
            return False
        
        ans = []
        for w in words:
            #print(pre,lens,w)
            if not w:   # 处理w == ''时无限循环的问题
                continue
            if check(w):
                ans.append(w)
            pre[w] = True
            l = len(w)
            if not lens or l != lens[-1]:
                lens.append(l)
        return ans
        '''

        # 方法3:字典树(排序优化) + 部分cache
        
        cache = dict()
        # 从cur中查找word[pos]
        def dfs(word,pos,cur):
            #print(word,pos,cur.keys())
            if pos == len(word):    # word的字符全部找到
                if '#' in cur:  # cnt > 0说明找到的不是word自身,# in cur说明是单词结尾
                    return True
                return False
            if '#' in cur:  # 一个单词结尾
                if word[pos:] not in cache:
                    cache[word[pos:]] = dfs(word,pos,tree)    # 从tree的开头再找
                if cache[word[pos:]]:
                    return True
            if word[pos] in cur:
                if dfs(word,pos + 1,cur[word[pos]]):
                    return True
            return False
        
        ans = []
        tree = dict()
        words.sort(key = len)
        #print(tree)
        for word in words:
            #print(word,tree,ans)
            if not word:   # 当w == ''时,cur['#'] = None相当于tree['#'] = None,会无限匹配
                continue
            if dfs(word,0,tree):
                cache[word] = True
                ans.append(word)
            cur = tree
            for c in word:
                cur = cur.setdefault(c,dict())
            cur['#'] = None  # 设置#为结束位标志
        return ans

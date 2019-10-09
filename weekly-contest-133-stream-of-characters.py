class StreamChecker:

    def __init__(self, words: List[str]):
        # 后缀树初始化
        self.d = {}
        # 遍历单词表
        for word in words:
            t = self.d
            # 生成后缀树
            for c in word[::-1]:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['end'] = True
        # 倒序串初始化
        self.pre = ''

    def query(self, letter: str) -> bool:
        # 倒序生成字符串
        self.pre = letter + self.pre
        t = self.d
        # 后缀树匹配
        for c in self.pre:
            if c not in t:
                return False
            t = t[c]
            if 'end' in t:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
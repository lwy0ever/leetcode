class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        one = []
        l = 0
        for w in words:
            # 如果不能加入新单词
            if l + len(w) > maxWidth:
                # 在结果中加入当前行
                if len(one) == 1:
                    ans.append(one[0] + ' ' * (maxWidth - l + 1))
                else:
                    #print(one,l)
                    d,m = divmod(maxWidth - l + 1,len(one) - 1)
                    # 由于l已经包含了一个空格的长度
                    # 所以每个单词间d + 1个空格,其中前m + 1个单词间d + 2个空格
                    t = (' ' * (d + 1)).join(one)
                    t = t.replace(' ' * (d + 1),' ' * (d + 2),m)
                    ans.append(t)
                # 清空当前行
                one = []
                l = 0
            # 
            one.append(w)
            l += len(w) + 1
        t = ' '.join(one)
        ans.append(t + ' ' * (maxWidth - l + 1))
        return ans
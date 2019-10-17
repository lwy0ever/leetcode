class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        cntS = [['',0]] # 补一个前缀,便于循环
        pre = ''
        for c in S:
            if c != pre:
                cntS.append([c,1])
                pre = c
            else:
                cntS[-1][1] += 1
        #print(cntS)
        ans = 0
        for w in words:
            pre = ''
            cnt = 0
            cur = 0
            for c in w:
                if c != pre:
                    #print(pre,cntS[cur][0],cnt,cntS[cur][1])
                    if pre == cntS[cur][0] and (cnt == cntS[cur][1] or (cnt < cntS[cur][1] and cntS[cur][1] >= 3)):
                        cnt = 1
                        cur += 1
                        pre = c
                    else:
                        # 不满足,检查下一个words
                        break
                else:
                    cnt += 1
            #print(cnt)
            # 检查最后一个字符
            if pre == cntS[cur][0] and (cnt == cntS[cur][1] or (cnt < cntS[cur][1] and cntS[cur][1] >= 3)) and cur == len(cntS) - 1:
                ans += 1
        return ans
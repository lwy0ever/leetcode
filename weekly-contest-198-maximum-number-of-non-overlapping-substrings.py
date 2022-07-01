class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # 对于某个满足条件2的子字符串,如果可以加前缀or后缀
        # 那么一定可以把前缀or后缀独立出去,使子字符串的数量增加
        
        # 先查找每个字符出现的起止位置
        charRange = dict()
        for i,c in enumerate(s):
            if c in charRange:
                charRange[c][1] = i
            else:
                charRange[c] = [i,i]
        #print(charRange)
        
        # 按照条件2,把必须合并的字符串合并起来
        #print(sorted(charRange.keys(),key = lambda x:charRange[x][1] - charRange[x][0]))
        # 优先合并最短的字符串,避免长字符串吃掉短字符串
        checked = set()
        for c in sorted(charRange.keys(),key = lambda x:charRange[x][1] - charRange[x][0]):
            if c not in charRange:
                continue
            checked.add(c)
            i = charRange[c][0] + 1
            while i < charRange[c][1]:
                #print(c,s[i],charRange[c],i,checked)
                if s[i] != c and s[i] in charRange and s[i] not in checked:
                    # 纯包含的,不合并
                    #if charRange[c][0] < charRange[s[i]][0] and charRange[s[i]][1] < charRange[c][1]:
                    #    continue
                    if charRange[s[i]][0] < charRange[c][0]:    # 由于合并,需要重新从开始位置检查
                        i = charRange[s[i]][0]
                    charRange[c] = [min(charRange[s[i]][0],charRange[c][0]),max(charRange[s[i]][1],charRange[c][1])]
                    del charRange[s[i]]
                i += 1
            #print(c,charRange)
        
        ranges = sorted(charRange.values())
        #print(ranges)
        
        n = len(ranges)
        ans = []
        
        def t(i,used):
            #print(f'enter:{i},{used}')
            if i >= n:
                nonlocal ans
                if len(used) > len(ans):
                    ans = used
                return
            for choice in range(i,n):
                if len(used) == 0 or ranges[used[-1]][1] < ranges[choice][0]:
                    # 可以选择ranges[choise]
                    break
            else:
                return
            # 考虑ranges[choice]
            #print(f'try:{i},{n},{choice + 1},{used}')
            if choice < n - 1 and ranges[choice][1] > ranges[choice + 1][0]:    # choice和choice + 1重叠,需要尝试放弃choice
                t(choice + 1,used)
            #print(f'try:{i},{n},{choice + 1},{used + [choice]}')
            t(choice + 1,used + [choice])
            
        t(0,[])
        
        return [s[ranges[i][0]:ranges[i][1] + 1] for i in ans]

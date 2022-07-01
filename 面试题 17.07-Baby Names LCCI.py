class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        # 并查集
        # 由于名字出现的顺序具有随机性,如果采用a并b的方式,却可能应该是b并a,而由于方向错误,出现连不上的情况
        # 做双向记录
        nameMap = collections.defaultdict(set)
        for s in synonyms:
            a,b = re.findall(r'\((.+),(.+)\)',s)[0]
            nameMap[a].add(b)
            nameMap[b].add(a)
        #print(nameMap)
        nameList = sorted(nameMap.keys())
        #print(nameList)

        nameParent = dict()
        # 使用bfs完成并查集
        for p in nameList:
            fromP = {p}
            while fromP:
                f = fromP.pop()
                while nameMap[f]:
                    t = nameMap[f].pop()
                    nameMap[t].remove(f)
                    nameParent[t] = f
                    fromP.add(t)
        #print(nameParent)            

        ans = collections.defaultdict(int)
        for n in names:
            name,cntStr = re.findall(r'(.+)\((\d+)\)',n)[0]
            cnt = int(cntStr)
            while name in nameParent:
                name = nameParent[name]
            ans[name] += cnt
        #print(ans)
        return [f'{k}({v})' for k,v in ans.items()]
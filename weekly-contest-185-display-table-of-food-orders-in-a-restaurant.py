class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        menus = set()
        d = collections.defaultdict(dict)
        for _,table,menu in orders:
            t = int(table)
            if menu in d[t]:
                d[t][menu] += 1
            else:
                d[t][menu] = 1
                menus.add(menu)
        #print(d)
        menuList = list(menus)
        menuList.sort()
        ans = []
        one = ['Table'] + menuList
        ans.append(one)
        for k in sorted(d.keys()):
            one = []
            one.append(str(k))
            for m in menuList:
                if m in d[k]:
                    one.append(str(d[k][m]))
                else:
                    one.append('0')
            ans.append(one)
        return ans
        
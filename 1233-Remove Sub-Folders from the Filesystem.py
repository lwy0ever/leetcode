class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # 优化
        # 对于排序后的folder,如果folder[i]有父文件夹,ans[-1]一定是其中一个
        folder.sort()
        ans = [folder[0]]
        n = len(folder)
        for i in range(1,n):
            preLen = len(ans[-1])
            if preLen >= len(folder[i]) or not (folder[i][:preLen] == ans[-1] and folder[i][preLen] == '/'):
                ans.append(folder[i])
        return ans

        # 排序
        folder.sort()
        #print(folder)
        ans = set()
        for path in folder:
            ps = path.split('/')
            father = ''
            for p in ps[1:]:
                father += '/' + p
                #print(path,father)
                if father in ans: # 父文件夹存在,删除
                    break
            else:
                ans.add(path)
        return list(ans)
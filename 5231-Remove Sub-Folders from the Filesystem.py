class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        father = set()
        folder.sort()
        for f in folder:
            t = ''
            for x in f.split('/')[1:]:
                t += '/' + x
                if t in father:
                    break
            else:
                father.add(t)
        return list(father)